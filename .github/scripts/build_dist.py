#!/usr/bin/env python3
# Builds the content of the dist branch: manifest.json and small previews.
#
# Usage: build_dist.py <repo folder> <owner/name> <output folder>
#
# Every folder in the repo root with an AUTHORS.md is a wallpaper pack:
#   <pack>/AUTHORS.md
#   <pack>/<variant folder>/<file>
# for example:
#   DriftAloft/DriftAloft-WL/DriftAloft-Aqua-WL.webp

import hashlib
import json
import os
import subprocess
import sys

from PIL import Image, ImageOps

PREVIEW_WIDTH = 400

# descriptors from CONTRIBUTING.md, spelled out for the wallpaper picker
CODES = {
    "WL": "With Logo",
    "WTL": "With Text Logo",
    "WNP": "No Particles",
    "WNTL": "No Text Logo",
}


def git(repo, *args):
    return subprocess.check_output(["git", "-C", repo] + list(args), text=True)


def read_authors_file(path):
    # # Drift Aloft
    #
    # Author: Ziednaga
    # Contact: https://github.com/Ziednaga
    # License: CC BY-NC 4.0
    #
    # ## Variants
    #
    # DriftAloft: Default
    # DriftAloft-WL: With Logo
    info = {"variants": {}}
    section = ""
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("## "):
                section = line[3:].strip().lower()
                continue
            if line.startswith("# ") and "title" not in info:
                info["title"] = line[2:].strip()
                continue
            key, _, value = line.partition(":")
            if not value:
                continue
            if section == "variants":
                info["variants"][key.strip()] = value.strip()
            elif key.strip().lower() in ("author", "contact", "license"):
                info[key.strip().lower()] = value.strip()
    return info


def readable(name):
    # Flat-Colors -> "Flat Colors", WNP-WL -> "No Particles With Logo"
    words = name.split("-")
    return " ".join(CODES.get(word, word) for word in words)


def sha256_of(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def save_preview(source, target):
    image = Image.open(source)
    image = ImageOps.exif_transpose(image)
    width, height = image.size

    preview_height = round(height * PREVIEW_WIDTH / width)
    preview = image.convert("RGB").resize((PREVIEW_WIDTH, preview_height))
    preview.save(target, "WEBP", quality=75)

    return width, height


def main():
    repo = sys.argv[1]
    slug = sys.argv[2]
    out = sys.argv[3]

    os.makedirs(os.path.join(out, "previews"), exist_ok=True)

    commit = git(repo, "rev-parse", "HEAD").strip()
    files = git(repo, "ls-files").splitlines()

    packs = {}

    for path in sorted(files):
        if not path.lower().endswith((".webp", ".png", ".jpg", ".jpeg")):
            continue

        parts = path.split("/")
        authors_file = os.path.join(repo, parts[0], "AUTHORS.md")
        if not os.path.isfile(authors_file):
            continue
        if len(parts) != 3:
            print("skipping", path)
            continue

        pack = parts[0]
        variant_folder = parts[1]
        file_name = parts[2]

        # DriftAloft -> "", DriftAloft-WL -> "WL", StarNet -> "StarNet"
        if variant_folder == pack:
            variant = ""
        else:
            variant = variant_folder.removeprefix(pack + "-")

        if pack not in packs:
            info = read_authors_file(authors_file)
            packs[pack] = {
                "id": pack,
                "name": info.get("title", pack),
                "author": info.get("author", ""),
                "contact": info.get("contact", ""),
                "license": info.get("license", ""),
                "variant_names": info["variants"],
                "variants": {},
            }

        # DriftAloft-Aqua-WL.webp -> "Aqua", Yvaga-3-Alt-Amethyst.webp -> "Amethyst"
        name = os.path.splitext(file_name)[0]
        name = name.removeprefix(pack + "-")
        if variant:
            name = name.removeprefix(variant + "-")
            name = name.removesuffix("-" + variant)

        full_path = os.path.join(repo, path)
        sha256 = sha256_of(full_path)
        preview = "previews/" + sha256[:16] + ".webp"
        width, height = save_preview(full_path, os.path.join(out, preview))
        print(path)

        variants = packs[pack]["variants"]
        if variant_folder not in variants:
            variants[variant_folder] = {"name": readable(variant), "items": []}

        variants[variant_folder]["items"].append({
            "name": readable(name),
            "path": path,
            "size": os.path.getsize(full_path),
            "sha256": sha256,
            "width": width,
            "height": height,
            "preview": preview,
        })

    pack_list = []
    for pack in packs.values():
        variants = pack["variants"]
        names = pack.pop("variant_names")

        # variants listed in AUTHORS.md come first, in that order, then the base variant
        order = [folder for folder in names if folder in variants]
        if pack["id"] in variants and pack["id"] not in order:
            order.append(pack["id"])
        order += [folder for folder in variants if folder not in order]

        variant_list = []
        for folder in order:
            variant = variants[folder]
            if folder in names:
                variant["name"] = names[folder]
            variant_list.append(variant)

        pack["variants"] = variant_list
        pack_list.append(pack)

    manifest = {
        "schema": 1,
        "commit": commit,
        "base_url": "https://raw.githubusercontent.com/" + slug + "/" + commit + "/",
        "packs": pack_list,
    }

    with open(os.path.join(out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
