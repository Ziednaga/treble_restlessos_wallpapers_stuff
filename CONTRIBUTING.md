# Contributing to RestlessOS Wallpapers

Thank you for wanting to contribute artwork to RestlessOS. This document explains how to submit your work so it integrates cleanly with the rest of the repository.

Every pack in this repository shows up in the RestlessOS wallpaper picker automatically once it is merged.

## Before you start

- All wallpapers must be original work.
- Do not submit AI-generated images, edits of other people's work, or copyrighted material.
- By submitting a Pull Request, you agree that your artwork will be distributed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license, consistent with the rest of this repository. This means anyone can share and adapt your work for non-commercial purposes as long as they give appropriate credit.

## Required format

| Property | Value |
| --- | --- |
| Resolution | 1440 × 3200 px or higher |
| Formats | WEBP (digital artwork), PNG or JPEG (photography). WEBP lossless is highly recommended. |
| Color profile | sRGB |

Submissions below 1440 × 3200 px will be rejected.

## Folder structure

Each wallpaper pack is a folder in the repository root. Folder and file names must not contain spaces.

```
YourWallpaperName/
  AUTHORS.md                          < Pack name and author (required)
  YourWallpaperName/                  < Base variant (required)
    YourWallpaperName-Silver.webp
    YourWallpaperName-Aqua.webp
    ...
  YourWallpaperName-WL/               < With RestlessOS Logo (optional)
    YourWallpaperName-Silver-WL.webp
    ...
  YourWallpaperName-WTL/              < With RestlessOS Text + Logo (optional)
    YourWallpaperName-Silver-WTL.webp
    ...
```

- The Base variant (no logo, no text) is the only required one.
- WL, WTL, WNP and WNTL variants are optional. Use them when your wallpaper uses the RestlessOS Logo or Text Logo, or to describe that it has no particles.

## AUTHORS.md

Every pack needs an `AUTHORS.md`. The build script (`.github/scripts/build_dist.py`) only treats a root folder as a wallpaper pack if it contains this file. A folder without it is ignored and its wallpapers never reach the wallpaper picker. It is also where the pack carries the attribution that CC BY-NC 4.0 asks for.

```
# Your Wallpaper Name

Author: YourName
Contact: https://github.com/YourGitHubUsername
License: CC BY-NC 4.0

## Variants

YourWallpaperName: Default
YourWallpaperName-WL: With Logo
YourWallpaperName-WTL: With Text Logo
```

How each part is used:

- **First line (`# ...`):** the pack name shown in the picker. Spaces are allowed here, unlike in folder and file names. Only the first `# ` line counts.
- **Author, Contact, License:** copied into the generated manifest, so every pack carries its attribution with it.
- **Variants (optional):** maps each variant folder to the name shown in the picker, in the order they should appear. Use it to describe what is different in each variant.

Rules that come from how the file is read:

- The name on the left must match the variant folder name exactly (case-sensitive). A name that does not match is ignored silently.
- Every line needs a name after the colon. A line without one is skipped, and that variant loses its place in the order.
- Variants that are not listed are still shown, after the listed ones, with a name built from the folder name. The base variant (the folder named like the pack) gets an empty name, which the app shows as "Default". A pack with a single variant folder does not need a `Variants` section. If a pack has several variants, list the base one first, because the first variant is the one the pack opens with and its first wallpaper is the pack cover.
- WL, WTL, WNP and WNTL are spelled out automatically when no name is given.

## Color naming

If your wallpaper has color variants, use only the following names. Minimum 1 variant, maximum 12.

| Name | Color |
| --- | --- |
| Silver | Grey |
| Titanium | Extremely pale or greyish blue |
| Aqua | Vivid turquoise or cyan |
| Copper | Deep red or reddish tones |
| Amethyst | Violet or lilac |
| Radio | Green |
| Gold | Yellow or golden |
| Sweet | Pink |
| Neon | Vivid blue or similar electric tone |
| Honey | Orange |
| Charcoal | Black |

## Other descriptors

- **Style and aesthetic:** Vintage, Retro, Neo, Minimal, Bold, Thin, Soft, Muted, Mono, Grainy, Blur, Ambient, Atmospheric, Dreamy, Clean, Flat, Sharp, Noise, Faded, Glow, Ethereal, Glass, Frosted, Translucent, Cyber, Industrial, Organic, Nord
- **Time of day:** Morning, Afternoon, Evening, Night, Dawn, Dusk
- **Seasonal:** Spring, Summer, Autumn, Winter
- **Technical:** Dark, Light, AMOLED
- **Sequential** (photo sets without hierarchy, or variants with slight differences such as Silver-A, Silver-B): A, B, C or I, II, III

You may combine descriptors when it makes sense:

```
WallpaperName-Copper-Vintage.webp
WallpaperName-Morning-WL.webp
WallpaperName-Mono-AMOLED.webp
WallpaperName-Amethyst-WL.webp
WallpaperName-Spring-WNP.webp
WallpaperName-Copper-WNTL.webp
WallpaperName-Neo-WL-WNTL.webp
WallpaperName-Dark-WNP-WL.webp
```

Neutral variants without a specific descriptor are fine too, for example `YourWallpaperName.webp` or `YourWallpaperName-Dark.webp`.

If none of the descriptors fits your work, propose a new one in an issue or in your Pull Request. It will be reviewed before merging. Do not use new descriptors without proposing them first, and avoid vague names like `WallpaperName-1.webp` or `WallpaperName-Final.webp`.

## File naming

```
WallpaperName-Descriptor.webp
WallpaperName-Descriptor-WL.webp      < With RestlessOS Logo
WallpaperName-Descriptor-WTL.webp     < With RestlessOS Text + Logo
WallpaperName-Descriptor-WNTL.webp    < Without Text Logo
WallpaperName-Descriptor-WNP.webp     < Without Particles and/or Post-Processing Effects
```

For Light and Dark versions:

```
WallpaperName-Descriptor-Dark.webp
WallpaperName-Descriptor-Dark-WL.webp
WallpaperName-Descriptor-Light-WTL.webp
```

**WNP** means the base image has no particles and/or post-processing effects applied over it, including but not limited to particles, blur, chromatic aberration, grain/noise, glow, vignetting and distortion.

## Compression

- Avoid excessive compression artifacts.
- WEBP submissions should preserve visual clarity, using WEBP lossless if possible.
- Do not upscale low-resolution images artificially.

## How to submit

1. Fork this repository.
2. Create your pack folder in the repository root, following the structure above.
3. Open a Pull Request with a short description of your wallpaper.
4. Wait for review. Feedback or merge will follow.

## What will be rejected

- Wrong resolution (below 1440 × 3200 px).
- AI-generated artwork or unauthorized edits of third-party work.
- Descriptors outside the lists above that were not proposed in the Pull Request.
- Folders or files with spaces or inconsistent naming.
- Packs without an `AUTHORS.md` or without the Base variant.

Create something unique, awesome and keep the repository clean.
