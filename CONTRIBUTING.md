
# Contributing to RestlessOS Wallpapers

Thank you for wanting to contribute artwork to RestlessOS. This document explains how to submit your work so it integrates cleanly with the rest of the repository.

Every pack in this repository shows up in the RestlessOS wallpaper picker automatically once it is merged.

## Before You Start

- All wallpapers must be original work.
- Do not submit AI-generated images, edits of other people's work, or copyrighted material.
- By submitting a Pull Request, you agree that your artwork will be distributed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license, consistent with the rest of this repository. This means anyone can share and adapt your work for non-commercial purposes as long as they give appropriate credit.

## Required Format

| Property | Value |
| --- | --- |
| Resolution | 1440 × 3200 px or higher |
| Formats | WEBP (digital artwork), PNG or JPEG (photography). Lossless WEBP is highly recommended. |
| Color profile | sRGB |

Submissions below 1440 × 3200 px will be rejected.

## Folder Structure

Each wallpaper pack is a folder in the repository root. Folder and file names must not contain spaces.

```text
YourWallpaperName/
  AUTHORS.md
  YourWallpaperName/
    YourWallpaperName-Silver.webp
    YourWallpaperName-Aqua.webp
  YourWallpaperName-WL/
    YourWallpaperName-Silver-WL.webp
  YourWallpaperName-WTL/
    YourWallpaperName-Silver-WTL.webp
  YourWallpaperName-WNTL/
    YourWallpaperName-Silver-WNTL.webp
  YourWallpaperName-WNP/
    YourWallpaperName-Silver-WNP.webp
```

- The base variant, without a logo or text, is the only required one.
- WL, WTL, WNP, and WNTL variants are optional.
- Use these variants to distinguish logo and text treatments or to provide versions without particles and/or post-processing effects.
- Every variant folder must follow the naming conventions described below.

## AUTHORS.md

Every pack needs an `AUTHORS.md`. The build script (`.github/scripts/build_dist.py`) only treats a root folder as a wallpaper pack if it contains this file. A folder without it is ignored and its wallpapers never reach the wallpaper picker. This file also carries the attribution required by the CC BY-NC 4.0 license.

```markdown
# Your Wallpaper Name

Author: YourName
Contact: https://github.com/YourGitHubUsername
License: CC BY-NC 4.0

## Variants

YourWallpaperName: Default
YourWallpaperName-WL: With Logo
YourWallpaperName-WTL: With Text Logo
```

### How AUTHORS.md Works

- **First heading (`# ...`):** The pack name shown in the picker. Spaces are allowed here, unlike in folder and file names. Only the first `# ` heading counts.
- **Author, Contact, License:** Copied into the generated manifest so every pack carries its attribution.
- **Variants (optional):** Maps each variant folder to the name shown in the picker, in the order they should appear.

### Variant Naming Rules

- The name on the left must match the variant folder name exactly, including capitalization. A name that does not match is ignored silently.
- Every line needs a name after the colon. A line without one is skipped, and that variant loses its specified place in the order.
- Variants that are not listed are still shown after the listed ones, with a name derived from the folder name. The base variant gets an empty name, which the app displays as `Default`.
- A pack with a single variant folder does not need a `Variants` section.
- If a pack has several variants, list the base variant first. The first variant determines which variant the pack opens with, and its first wallpaper becomes the pack cover.
- WL, WTL, WNP, and WNTL are spelled out automatically when no custom name is provided.

## Color Naming

If your wallpaper has color variants, use only the following names. Minimum 1 variant, maximum 18.

| Name | Color |
| --- | --- |
| Silver | Grey |
| Titanium | Extremely pale or greyish cyan |
| Aqua | Vivid turquoise or cyan |
| Copper | Deep red or reddish tones |
| Amethyst | Violet or lilac |
| Radio | Green |
| Gold | Yellow or golden |
| Sweet | Pink |
| Neon | Vivid blue or similar electric tone |
| Honey | Orange |
| Charcoal | Black |
| Pearl | White |
| Azure | Sky blue or bright cerulean |
| Teal | Emerald green |
| Coral | Reddish pink |
| Sapphire | Darker blue |
| Mocha | Brown |
| Orchid | Magenta |

Use these names only for color variants. Do not use them as substitutes for aesthetic or technical descriptors.

## Style and Design

- **Style:** Vintage, Natural, Urban, FreeStyle, Retro, Neo, Minimal, Bold, Thin, Flat, Clean, Sharp, Organic, Industrial, Cyber, Cosmic, Surreal, Mono
- **Shapes and Patterns:** Geometric, Fluid, Fractal, Symmetric, Asymmetric, Centered, Layered
- **Materials and Appearance:** Glass, Frosted, Translucent, Metallic, Iridescent, Pearlescent
- **Texture and Effects:** Grainy, Noise, Blur, Glow, Glitch, Faded, Distortion
- **Mood and Atmosphere:** Soft, Muted, Ambient, Atmospheric, Dreamy, Ethereal, Nord

## Time of Day

Morning, Afternoon, Evening, Night, Dawn, Dusk

## Seasonal

Spring, Summer, Autumn, Winter

## Weather

Sunshine, Cloudy, Raining, PartlyCloudy, Overcast, Snowy, Foggy, Thunder, Windy

## Technical

Dark, Light, AMOLED

Use `Dark` and `Light` to distinguish overall tonal variants. Use `AMOLED` when the artwork is specifically designed for dark displays, such as through predominantly black areas intended to reduce power consumption on AMOLED screens.

## Sequential Variants

Use `A`, `B`, `C` or `I`, `II`, `III` for photo sets without a hierarchy or for closely related variants with minor differences.

Sequential labels should be used only when no more descriptive name is appropriate.

## Combining Descriptors

Descriptors may be combined when each adds meaningful information.

Examples:

```text
WallpaperName-Copper-Vintage.webp
WallpaperName-Morning-WL.webp
WallpaperName-Mono-AMOLED.webp
WallpaperName-Amethyst-WL.webp
WallpaperName-Spring-WNP.webp
WallpaperName-Copper-WNTL.webp
WallpaperName-Neo-WL-WNTL.webp
WallpaperName-Dark-WNP-WL.webp
WallpaperName-Geometric-Silver.webp
WallpaperName-Fluid-Amethyst.webp
WallpaperName-Cosmic-Night.webp
```

Neutral variants without a specific descriptor are also acceptable:

```text
YourWallpaperName.webp
YourWallpaperName-Dark.webp
```

Do not introduce new descriptors without proposing them in an Issue or Pull Request. New descriptors will be reviewed before being accepted into this document.


### Filename Parsing and Manifest Names

The build script derives wallpaper display names from their filenames. It removes the pack name prefix and, when applicable, the variant code associated with the containing folder. Remaining hyphen-separated words are converted into a readable name in the wallpaper picker.

Use the following naming convention:

```text
PackName/PackName-Descriptor.webp
PackName/PackName-Descriptor-AdditionalDescriptor.webp
PackName-WL/PackName-WL-Descriptor.webp
PackName-WTL/PackName-WTL-Descriptor.webp
PackName-WNTL/PackName-WNTL-Descriptor.webp
PackName-WNP/PackName-WNP-Descriptor.webp
```

Examples:

```text
DriftAloft/DriftAloft-Aqua.webp
DriftAloft/DriftAloft-Copper-Vintage.webp
DriftAloft-WL/DriftAloft-WL-Aqua.webp
DriftAloft-WTL/DriftAloft-WTL-Amethyst.webp
DriftAloft-WNTL/DriftAloft-WNTL-Silver.webp
DriftAloft-WNP/DriftAloft-WNP-Geometric.webp
```

The variant code must match the containing variant folder. Place the code immediately after the pack name in the filename so the build script can remove it correctly.

Do not place the variant code at the end of the filename. The script does not automatically remove trailing variant codes from filenames, which can cause them to appear in the wallpaper's display name.

The order of wallpapers within a variant is determined by the sorted file paths, not by the order in which files are listed in AUTHORS.md.

### Light and Dark Variants

```text
WallpaperName-Descriptor-Dark.webp
WallpaperName-Descriptor-Dark-WL.webp
WallpaperName-Descriptor-Light-WTL.webp
```

### WNP: Without Particles and/or Post-Processing Effects

WNP identifies a version without particles and/or post-processing effects applied over the base artwork. This includes, but is not limited to:

- Particles
- Blur
- Chromatic aberration
- Grain or noise
- Glow
- Vignetting
- Distortion

Use WNP when the corresponding particles and/or post-processing effects are absent. The artwork does not have to be completely unprocessed.

- "This particular versión from my wallpaper pack doesn't have blur, but the base versión has it"

## Compression and Image Quality

- Avoid excessive compression artifacts.
- WEBP submissions should preserve visual clarity. Lossless WEBP is recommended whenever practical.
- Do not artificially upscale low-resolution images to meet the minimum resolution requirement. AI-based upscaling must not be used to disguise artwork that does not meet the required resolution.
- Ensure the final image uses the sRGB color profile.
- Inspect gradients, smooth transitions, and fine details for visible banding, noise, or compression artifacts before submitting.

## How to Submit

1. Fork this repository.
2. Create your wallpaper pack in the repository root.
3. Add the required `AUTHORS.md` file and base variant folder.
4. Follow the folder, file, color, and descriptor naming conventions.
5. Open a Pull Request with a short description of your wallpaper and its variants.
6. Wait for review and address any requested changes.

## What Will Be Rejected

Submissions may be rejected for any of the following reasons:

- Resolution below 1440 × 3200 px.
- AI-generated artwork or unauthorized edits of third-party work.
- Use of unapproved descriptors.
- Folder or file names containing spaces or inconsistent naming.
- Missing `AUTHORS.md` or base variant folder.
- Excessive compression artifacts or artificially upscaled images.
- Incorrect color profile or other violations of the required format.

Create something unique, keep the repository clean, and make every pixel count.
