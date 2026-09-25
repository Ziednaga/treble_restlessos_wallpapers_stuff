### Contributing to RestlessOS Wallpapers
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
-- Thank you for wanting to contribute artwork to RestlessOS.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
-- This document explains exactly how to submit your work, 
so it integrates cleanly with the rest of the repository.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## Before You Start:
All wallpapers must be original work. 

-- Do not submit AI-generated images, edits of other people's work, or copyrighted material.

-- By submitting a Pull Request, you agree that your artwork 
will be distributed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license, 
consistent with the rest of this repository. 

-- This means anyone can share and adapt your work.
for non-commercial purposes as long as they give appropriate credit.

>>>>>>>>>>>>>>>>
### Required Format:
```
Property    Value
Resolution: 1440 × 3200 px (or higher)
Formats accepted:  WEBP (Digital artwork), PNG or JPEG (Photography) (We highly recommend WEBP lossless format)
Color profile: sRGB
```
>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>
### Required at least 1440x3200 as minimum. Submissions below this resolution will be rejected.
>>>>>>>>>>>>>>>>
### Folder Structure
-- Your submission goes inside `Wallpapers/[Your-Username]/` and contains an example of `Author.txt`.
-- Follow the exact same conventions used in the main wallpapers.
```
/Wallpapers/
  [Your-Username]/
    YourWallpaperName-Wallpaper/
    AUTHORS.txt                           < Declare your atributtion
      YourWallpaperName/                  < Base variant (required)
          YourWallpaperName-Silver.webp
          YourWallpaperName-Aqua.webp
          ...
      YourWallpaperName-WL/               < With Restless Logo variant (optional)
          YourWallpaperName-Silver-WL.webp
          ...
      YourWallpaperName-WTL/              < With RestlessOS Text + Logo variant (optional)
          YourWallpaperName-Silver-WTL.webp
          ...
       YourWallpaperName-ABC.../
          ...
```
-- The Base variant (no logo, no text) is the only required one. 

-- WL, WTL, WNP and WNTL variants are optional. Use them when your wallpaper uses RestlessOS Logo and RestlessOS Text Logo or needs to describe it doesn't have particles.
>>>>>>>>>>>>>>>>
### Color Naming Convention
If your wallpaper has color variants, use only the following names. 

--Minimum: 1 variant. Maximum: 12 variants.

### Color reference:
```
---Silver: Grey
---Titanium: Extremely pale or greyish blue
---Aqua: Vivid turquoise or cyan
---Copper :Deep red or reddish tones
---Amethyst: Violet or lilac
---Radio: Green
---Gold: Yellow or golden
---Sweet: Pink
---Neon: Vivid blue or similar electric tone
---Honey: Orange
---Charcoal: Black
```
>>>>>>>>>>>>>>>>>>
### Style & Aesthetic variants:
---Vintage / Retro / Neo / Minimal / Bold / Thin / Soft / Muted / Mono / Grainy / Blur / Ambient / Atmospheric / Dreamy / Clean / Flat / Sharp / Noise / Faded / Glow / Ethereal / Glass / Frosted / Translucent / Cyber / Industrial / Organic / Nord /
>>>>>>>>>>>>>>>>>>
### Time-of-day & Ambient variants:
---Morning / Afternoon / Evening / Night / Dawn / Dusk
>>>>>>>>>>>>>>>>>>
### Seasonal variants:
---Spring / Summer / Autumn / Winter
>>>>>>>>>>>>>>>>>>
### Technical variants:
---Dark / Light / AMOLED /
>>>>>>>>>>>>>>>>>>
### Sequential variants (for photo sets without hierarchy or variants with slight differences (silver-A; Silver-B...):
---A / B / C  or  I / II / III /
>>>>>>>>>>>>>>>>>>
-- You may combine descriptors when it makes sense:
```
WallpaperName-Copper-Vintage.webp
WallpaperName-Morning-WL.webp
WallpaperName-Mono-AMOLED.webp

WallpaperName-Amethyst-WL.webp
WallpaperName-Spring-WNP.webp
WallpaperName-Copper-WNTL.webp

WallpaperName-Neo-WL-WNTL.webp
WallpaperName-Dark-WNP-WL.webp
WallpaperName-Dusk-WNT-WNP.webp
```
-- You may also include neutral variants
(no specific descriptor, e.g. a base colorless version).
Name them descriptively > for example:
```
YourWallpaperName.webp or YourWallpaperName-Dark.webp.
```
-- If none of the above fits your work, you may propose a new descriptor (open an issue).
in your Pull Request. It will be reviewed before merging.

### Do not invent new variant names without proposing them first.
### Avoid vague or arbitrary names like `WallpaperName-1.webp` or `WallpaperName-Final.webp`
>>>>>>>>>>>>>>>>>>
### File Naming
Follow this pattern exactly:
```
WallpaperName-Descriptor.webp
WallpaperName-Descriptor-WL.webp      < With RestlessOS Logo
WallpaperName-Descriptor-WTL.webp     < With RestlessOS Text + Logo
WallpaperName-Descriptor-WNTL.webp     < Without Text Logo
WallpaperName-Descriptor-WNP.webp     < Without Particles or/and Post-Processing Effects
```
>>>>>>>>>>>>>>>>>>
### WNP (Without Particles or/and Post-Processing Effects) Definition

-- WNP refers to the absence of particles and/or post-processing effects 
applied over the base image, including but not limited to: particles, 
blur, chromatic aberration, grain/noise, glow, vignetting, and 
distortion.
>>>>>>>>>>>>>>>>>>
--- Does your wallpaper have Light/Dark variations?
```
WallpaperName-Descriptor-Dark/Light.png
WallpaperName-Descriptor-Dark/Light-WL.png      < Dark/Light With Logo
WallpaperName-Descriptor-Dark/Light-WTL.png     < Dark/Light With Text + Logo
WallpaperName-Descriptor-Dark/Light-WNTL.png     < Dark/Light Without Text 
WallpaperName-Descriptor-Dark/Light-WNP.png     < Dark/Light Without Particles
```
>>>>>>>>>>>>>>>>>>
### Compression Guidelines

-- Avoid excessive compression artifacts.

-- WEBP submissions should preserve visual clarity using (if is possible) `webp-lossless`.

-- Do not upscale low-resolution images artificially.
>>>>>>>>>>>>>>>>>>
### How to Submit?

-- Fork this repository.

-- Create your folder under
`/Wallpapers/` following the structure above.

-- Open a Pull Request with a short description of your wallpaper.

-- Wait for review > feedback or merge will follow.

>>>>>>>>>>>>>>>>>>
### What Will Be Rejected?

-- Wrong resolution (below 1440 × 3200 px).

-- AI-generated artwork or unauthorized edits of third-party work.

-- Variant names outside the defined lists or not proposed in the Pull Request.

-- Folders or files with spaces or inconsistent naming.

-- Submissions that don't include at least the Base variant.

>>>>>>>>>>>>>>>>>>
## Create something unique, awesome and keep the repository clean.