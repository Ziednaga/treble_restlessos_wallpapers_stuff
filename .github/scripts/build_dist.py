#!/usr/bin/env python3
# Builds the content of the dist branch: manifest.json and small previews.
#
# Usage: build_dist.py <repo folder> <owner/name> <output folder>
#
# Wallpapers are expected at:
#   Wallpapers/<author>/<pack>-Wallpaper/<variant folder>/<file>
# for example:
#   Wallpapers/Ziednaga/DriftAloft-Wallpaper/DriftAloft-WL/DriftAloft-Aqua-WL.webp

import hashlib
import json
import os
import subprocess
import sys

from PIL import Image, ImageOps

PREVIEW_WIDTH = 400


def git(repo, *args):
    return subprocess.check_output(["git", "-C", repo] + list(args), text=True)


def read_file_lines(path):
    if not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


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
    files = git(repo, "ls-files", "Wallpapers").splitlines()

    authors = {}
    packs = {}

    for path in sorted(files):
        if not path.lower().endswith((".webp", ".png", ".jpg", ".jpeg")):
            continue

        parts = path.split("/")
        if len(parts) != 5 or not parts[2].endswith("-Wallpaper"):
            print("skipping", path)
            continue

        author = parts[1]
        pack = parts[2].removesuffix("-Wallpaper")
        variant_folder = parts[3]
        file_name = parts[4]

        # DriftAloft -> "", DriftAloft-WL -> "WL", StarNet -> "StarNet"
        if variant_folder == pack:
            variant = ""
        else:
            variant = variant_folder.removeprefix(pack + "-")

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

        if author not in authors:
            authors[author] = read_file_lines(os.path.join(repo, "Wallpapers", author, "AUTHORS.txt"))

        pack_id = author + "/" + pack
        if pack_id not in packs:
            packs[pack_id] = {"id": pack_id, "name": pack, "author": author, "variants": {}}

        variants = packs[pack_id]["variants"]
        if variant not in variants:
            variants[variant] = []

        variants[variant].append({
            "name": name,
            "path": path,
            "size": os.path.getsize(full_path),
            "sha256": sha256,
            "width": width,
            "height": height,
            "preview": preview,
        })

    pack_list = []
    for pack in packs.values():
        variant_list = []

        # the base variant ("") comes first
        if "" in pack["variants"]:
            variant_list.append({"name": "", "items": pack["variants"].pop("")})

        for variant_name, items in pack["variants"].items():
            variant_list.append({"name": variant_name, "items": items})

        pack["variants"] = variant_list
        pack_list.append(pack)

    manifest = {
        "schema": 1,
        "commit": commit,
        "base_url": "https://raw.githubusercontent.com/" + slug + "/" + commit + "/",
        "authors": authors,
        "packs": pack_list,
    }

    with open(os.path.join(out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
