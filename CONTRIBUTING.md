
# Contributing to RestlessOS Wallpapers

Thank you for contributing artwork to RestlessOS. This document explains how to prepare, name, and submit wallpaper packs so they integrate cleanly with the repository.

Every accepted pack is automatically included in the RestlessOS wallpaper picker when merged.

## 1. Contribution Requirements

- All wallpapers must be original work.
- Do not submit AI-generated images, edits of other people's work, or copyrighted material.
- By submitting a Pull Request, you agree that your artwork will be distributed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license, consistent with the rest of this repository.
- This license allows others to share and adapt your work for non-commercial purposes, provided they give appropriate credit.

### Required Image Format

| Property | Requirement |
| --- | --- |
| Resolution | 1440 × 3200 px or higher |
| Formats | WEBP for digital artwork; PNG or JPEG for photography |
| Color profile | sRGB |
| Compression | Lossless WEBP is highly recommended |

Submissions below 1440 × 3200 px will be rejected.

## 2. Wallpaper Pack Structure

Each wallpaper pack must be a folder in the repository root. Folder and file names must not contain spaces.

```text
YourWallpaperName/
├── AUTHORS.md
├── YourWallpaperName/
│   ├── YourWallpaperName-Silver.webp
│   └── YourWallpaperName-Aqua.webp
├── YourWallpaperName-WL/
│   └── YourWallpaperName-WL-Silver.webp
├── YourWallpaperName-WTL/
│   └── YourWallpaperName-WTL-Silver.webp
├── YourWallpaperName-WNTL/
│   └── YourWallpaperName-WNTL-Silver.webp
└── YourWallpaperName-WNP/
    └── YourWallpaperName-WNP-Silver.webp
```

- `AUTHORS.md` is mandatory.
- The base variant, stored in the folder matching the pack name, is mandatory.
- Additional variant folders are optional.
- Each variant folder must follow the naming conventions described in Section 4.

## 3. AUTHORS.md and Manifest Ordering

The build script, `.github/scripts/build_dist.py`, uses `AUTHORS.md` to identify wallpaper packs, retrieve attribution, and determine the display names and ordering of variants.

A folder without `AUTHORS.md` is not recognized as a wallpaper pack.

### Example

```markdown
# Your Wallpaper Name

Author: YourName
Contact: https://github.com/YourGitHubUsername
License: CC BY-NC 4.0

## Variants

YourWallpaperName: Default
YourWallpaperName-WL: With Logo
YourWallpaperName-WTL: With Text Logo
YourWallpaperName-WNP: No Particles
YourWallpaperName-WNTL: No Text Logo
```

### How It Works

- **First heading:** The first `# ` heading provides the pack name displayed in the picker. Spaces are allowed here.
- **Author, Contact, License:** These fields provide attribution in the generated manifest.
- **Variants:** Each entry maps a variant folder to its display name.
- **Variant order:** Variants listed in this section appear in the specified order. List the base variant first if it should be the default opening variant.
- **Cover image:** The first wallpaper in the first displayed variant becomes the pack cover.
- **Unlisted variants:** These are still included after listed variants, with names derived from their folder names. The base variant is displayed as `Default` when its name is empty.
- **Missing display names:** Entries without a name after the colon are skipped.
- **Exact folder names:** Variant names on the left must match their folder names exactly, including capitalization.
- **Single-variant packs:** A `Variants` section is unnecessary if the pack has only one variant folder.

The order of wallpaper files within each variant is determined by lexicographic sorting of their paths. Listing files in `AUTHORS.md` does not control their order.

## 4. File and Variant Naming

Use hyphens to separate the pack name, variant codes, and descriptive labels. Keep names consistent throughout the pack.

### 4.1 Variant Codes

These codes identify technical or compositional variants:

| Code | Meaning |
| --- | --- |
| `WL` | With Logo |
| `WTL` | With Text Logo |
| `WNTL` | Without Text Logo |
| `WNP` | Without Particles and/or Post-Processing Effects |

These codes are naming conventions. The build script converts them into readable display names but does not inspect the artwork to verify their visual meaning. Contributors and reviewers are responsible for ensuring that the artwork matches its description.

##
### 4.2 Filename Structure

The filename consists of the pack name followed by descriptive labels and, when applicable, variant codes. Separate each component with hyphens.

Variant codes may appear before or after descriptive labels. Both conventions are supported by the repository, provided the filename matches the variant folder and the build script can identify the variant code.

```text
PackName/PackName-Descriptor.webp
PackName/PackName-Descriptor-AdditionalDescriptor.webp

PackName-WL/PackName-Descriptor-WL.webp
PackName-WL/PackName-WL-Descriptor.webp

PackName-WTL/PackName-Descriptor-WTL.webp
PackName-WNP/PackName-Descriptor-WNP.webp
PackName-WNTL/PackName-Descriptor-WNTL.webp
```

Examples from existing naming patterns:

```text
BeatYourRhythm/BeatYourRhythm-Amethyst.webp
BeatYourRhythm-WL/BeatYourRhythm-Amethyst-WL.webp
DearPrudence-Vintage/DearPrudence-Vintage-A.webp
MadeInEden/MadeInEden-WNP-WL.webp
```

The variant code must match the containing variant folder. Keep filenames consistent within each pack and avoid placing variant codes in the base variant folder unless they are intentionally part of the filename's descriptive text.

### 4.3 How Display Names Are Generated

The build script derives wallpaper display names from their paths and filenames:

1. Removes the file extension.
2. Removes the pack name prefix.
3. Removes the matching variant code from the beginning or end of the remaining filename, when applicable.
4. Converts recognized codes into readable labels and formats the remaining hyphen-separated words.

For example:

```text
DriftAloft/DriftAloft-Copper-Vintage.webp
>> Copper Vintage

DriftAloft-WL/DriftAloft-WL-Aqua.webp
>> Aqua

DriftAloft-WL/DriftAloft-Aqua-WL.webp
>> Aqua
```

The script does not inspect the image itself. It derives names from filenames and folder structure, so inconsistent naming can produce unintended display names.

### 4.4 Light and Dark Variants

Use `Light` and `Dark` to distinguish overall tonal versions of the artwork.

```text
WallpaperName-Descriptor-Dark.webp
WallpaperName-Descriptor-Dark-WL.webp
WallpaperName-Descriptor-Light-WTL.webp
```

These are descriptive labels, not variant folder codes. When a wallpaper has a specific logo treatment, place it in the corresponding variant folder.

## 5. Descriptor Guidelines

Descriptors communicate the artwork's visual characteristics. Use existing descriptors whenever possible, and combine them only when each adds meaningful information.

### 5.1 Color

Use only the following approved color names for color variants. Minimum: 1. Maximum: 18.

| Name | Intended Color |
| --- | --- |
| `Silver` | Grey |
| `Titanium` | Extremely pale or greyish cyan |
| `Aqua` | Vivid turquoise or cyan |
| `Copper` | Deep red or reddish tones |
| `Amethyst` | Violet or lilac |
| `Radio` | Green |
| `Gold` | Yellow or golden |
| `Sweet` | Pink |
| `Neon` | Vivid blue or similar electric tone |
| `Honey` | Orange |
| `Charcoal` | Black |
| `Pearl` | White |
| `Azure` | Sky blue or bright cerulean |
| `Teal` | Emerald green |
| `Coral` | Reddish pink |
| `Sapphire` | Darker blue |
| `Mocha` | Brown |
| `Orchid` | Magenta |

Use these names only for color variants. Do not use them as substitutes for aesthetic or technical descriptors.

### 5.2 Style and Design

Use these descriptors to describe the overall visual style or design language.

`Vintage`, `Natural`, `Urban`, `FreeStyle`, `Retro`, `Neo`, `Minimal`, `Bold`, `Thin`, `Flat`, `Clean`, `Sharp`, `Organic`, `Industrial`, `Cyber`, `Cosmic`, `Surreal`, `Mono`

### 5.3 Shapes and Patterns

Use these descriptors for composition, geometry, and recurring visual structures.

`Geometric`, `Fluid`, `Fractal`, `Symmetric`, `Asymmetric`, `Centered`, `Layered`

### 5.4 Materials and Appearance

Use these descriptors for material qualities and surface appearance.

`Glass`, `Frosted`, `Translucent`, `Metallic`, `Iridescent`, `Pearlescent`

### 5.5 Texture and Effects

Use these descriptors for visible textures and applied effects.

`Grainy`, `Noise`, `Blur`, `Glow`, `Glitch`, `Faded`, `Distortion`

### 5.6 Mood and Atmosphere

Use these descriptors for the emotional or atmospheric character of the artwork.

`Soft`, `Muted`, `Ambient`, `Atmospheric`, `Dreamy`, `Ethereal`, `Nord`

### 5.7 Time of Day

`Morning`, `Afternoon`, `Evening`, `Night`, `Dawn`, `Dusk`

### 5.8 Seasons

`Spring`, `Summer`, `Autumn`, `Winter`

### 5.9 Weather

`Sunshine`, `Cloudy`, `Raining`, `PartlyCloudy`, `Overcast`, `Snowy`, `Foggy`, `Thunder`, `Windy`

### 5.10 Display and Technical Characteristics

`Dark`, `Light`, `AMOLED`

Use `Dark` and `Light` to distinguish overall tonal variants. Use `AMOLED` when the artwork is specifically designed for dark displays, such as through predominantly black areas intended to reduce power consumption on AMOLED screens.

### 5.11 Sequential Variants

Use `A`, `B`, `C` or `I`, `II`, `III` for photo sets without a hierarchy or closely related variants with minor differences.

Use sequential labels only when no more descriptive name is appropriate.

### 5.12 Combining Descriptors

Descriptors may be combined when each adds meaningful information.

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

Do not introduce new descriptors without proposing them in an Issue or Pull Request. New descriptors will be reviewed before being added to this document.

## 6. WNP: Without Particles and/or Post-Processing Effects

`WNP` identifies a version without particles and/or post-processing effects applied over the base artwork.

This can include, but is not limited to:

- Particles
- Blur
- Chromatic aberration
- Grain or noise
- Glow
- Vignetting
- Distortion

Use `WNP` when the corresponding particles and/or post-processing effects are absent. The artwork does not have to be completely unprocessed.

For example, a wallpaper pack may contain a base version with blur and a `WNP` version without that blur.

## 7. Compression and Image Quality

- Avoid excessive compression artifacts.
- Preserve visual clarity in WEBP submissions. Lossless WEBP is recommended whenever practical.
- Do not artificially upscale low-resolution images to meet the minimum resolution requirement.
- AI-based upscaling must not be used to disguise artwork that does not meet the required resolution.
- Ensure the final image uses the sRGB color profile.
- Inspect gradients, smooth transitions, and fine details for visible banding, noise, or compression artifacts before submitting.

## 8. How to Submit

1. Fork this repository.
2. Create your wallpaper pack in the repository root.
3. Add the required `AUTHORS.md` file and base variant folder.
4. Follow the folder, file, variant, color, and descriptor naming conventions.
5. Open a Pull Request with a short description of your artwork and its variants.
6. Wait for review and address any requested changes.

## 9. Reasons for Rejection

Submissions may be rejected for any of the following reasons:

- Resolution below 1440 × 3200 px.
- AI-generated artwork or unauthorized edits of third-party work.
- Unapproved descriptors.
- Folder or file names containing spaces or inconsistent naming.
- Missing `AUTHORS.md` or base variant folder.
- Excessive compression artifacts or artificially upscaled images.
- Incorrect color profile or other violations of the required format.

Create something unique, keep the repository clean, and make every pixel count.
