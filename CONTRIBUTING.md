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

Every pack needs an `AUTHORS.md`. The first line is the pack name as it is shown in the wallpaper picker, so spaces are allowed there.

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

The `Variants` section is optional. It maps each variant folder to the name shown in the wallpaper picker, in the order they should appear. Use it to describe what is different in each variant. WL, WTL, WNP and WNTL are spelled out automatically when no name is given.

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
