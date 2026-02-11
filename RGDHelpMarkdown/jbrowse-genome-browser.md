---
source_url: https://rgd.mcw.edu/wg/help3/tools/rgd-genome-browsers/the-rat-jbrowse-genome-browser
tool_url: https://rgd.mcw.edu/jbrowse/
---

# RGD JBrowse Genome Browser Help

## Overview

JBrowse is an interactive genome browser that prioritizes the browser display while consolidating menu and header regions. It provides comprehensive genomic data visualization capabilities.

## Selecting a Map/Assembly

RGD currently has JBrowse instances for:
- Rat genome assemblies: RGSC 3.4, RGSC 5.0, RGSC 6.0
- Mouse: build 37
- Human: builds 36.3 and 37

The assembly dropdown is located in the top menu bar.

## The Search Box

The search feature offers autocomplete suggestions based on typed text:
- **Gene symbol search** - Type a gene symbol (e.g., "Ucp") to get suggestions (Ucp1, Ucp2, Ucp3, etc.)
- **Positional search** - Use format "Chr#:start..stop" with optional comma separators

## Selecting Tracks

Tracks appear in a left sidebar organized by categories shown on grey backgrounds with track counts:
- Categories can be expanded/collapsed
- Checkboxes control track visibility
- A filter box at the top allows searching tracks by keyword
- A red X clears filters

## Navigation Features

### Position Bars
- **Upper grey bar** - Shows chromosomal position with a red line/box
- **Lower bar** - Displays the detail view area with light blue connecting lines

### Navigation Controls
- Arrow buttons move the view one screen width left or right
- Larger zoom buttons zoom approximately twice as far
- Click-and-drag selection works on both position bars
- Click and drag in unoccupied browser areas to move the display

## Context-Specific Track Menus

Click the down arrow on a track title bar to access:
- **About this track** - Track type and category information
- **Pin to top** - Keeps track at the top of the browser
- **Edit Config** - Direct configuration script editing (advanced users)
- **Delete track** - Removes the track
- **Save Track Data** - View/save track data for current region or entire chromosome
- **Display mode** - Normal, Compact, or Collapse viewing options
- **Show labels** - Toggle object labels on/off

### Saving Track Data
You can save data for the current region or, for some tracks, the entire chromosome. Large datasets like strain-specific variants offer VCF files on the FTP site instead.

## Highlighting Regions

### Method 1: Menu
Use View > Set Highlight and enter "Chr#:start..stop" format. Regions appear highlighted in yellow across all tracks.

### Method 2: Button
Click the "Highlight a region" button right of the search box, then click and drag in the browser window.

**Notes:**
- Do not drag on the position bar (this zooms instead of highlighting)
- Only one region can be highlighted at a time
- The browser won't automatically navigate to off-screen highlights

## FASTA Sequence Extraction

1. Navigate to your region of interest
2. Turn on the sequence track (for RGSC 5.0, find "rn5 DNA" under "Reference Data")
3. Even when the browser shows "Zoom in to see sequence," you can still view and save FASTA sequences using "Save Track Data"

## Sharing JBrowse Views

Click the "Share" button in the top right corner of the blue menu bar to obtain a shareable URL. The URL opens the interactive browser itself (not an image), allowing recipients to manipulate tracks and regions.

## What's New in JBrowse

### Strain-Specific Variant Tracks
Now in the general "Variants" category, listed alphabetically by strain symbol with sequencing institution abbreviations.

### RNA-Seq BAM Alignment Tracks
Complete BAM alignments between RNA-Seq reads and reference genome sequences. JBrowse handles large datasets better than the legacy GBrowse.

### Gene Predictions Based on RNA-Seq Data
Includes gene predictions based on RNA-Seq data with and without ESTs, showing predictions from bone marrow, brain, and kidney tissues.
