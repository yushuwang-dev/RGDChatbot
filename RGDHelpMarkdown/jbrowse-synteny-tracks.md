---
source_url: https://rgd.mcw.edu/wg/help3/tools/rgd-genome-browsers/the-rat-jbrowse-genome-browser/more-about-jbrowse-tracks/synteny-tracks
tool_url: https://rgd.mcw.edu/jbrowse/
---

# RGD JBrowse Synteny Tracks

## Overview

Synteny tracks are available in specific JBrowse versions, particularly the rat RGSC 3.4 JBrowse. They display blocks of synteny between rat, mouse, and human, and between rat v3.4 and rat v5.0.

## What is Synteny?

Synteny refers to the occurrence of genes on the same chromosome. Conserved synteny refers to the occurrence of synteny of orthologous genes in different organisms. Synteny blocks represent regions of chromosomes that are conserved between species.

## How to Access Synteny Tracks

1. In the Available Tracks list, click "Synteny"
2. Select from the synteny group options:
   - Rat v3.4 versus mouse v37 and human v36
   - Rat v3.4 versus mouse v37 and human v37
   - Rat v3.4 versus rat v5.0
3. Choose desired track(s)

## Visual Representation

Synteny blocks display as colored bars. The colors denote the matching chromosome in the other species or assembly, following UCSC standard color codes. Arrows on block ends indicate directional gene order relative to the displayed rat chromosome.

## Chromosome Color Codes

Colors follow the UCSC standard encoding with 29 chromosomes/regions (Chr 1-22, X, Y) each assigned a unique color from Golden Brown (#996600) to Silver (#CCCCCC).

## Synteny Track Popup Information

Clicking a synteny block reveals details about syntenic regions in both originating and target species/assemblies:

- **Source:** "synteny"
- **Class:** Target species and assembly identification
- **Genome location:** Full position (Chr:Start..Stop format) linking to full syntenic region
- **Feature length:** Base pair length in originating species/assembly
- **Synteny Block ID:** Numerical identifier in target species/assembly
- **Corresponding Location:** Target genomic position, linking to JBrowse view in target species
- **Synteny Block Length:** Base pair length in target species/assembly

## Usage Tips

- Synteny tracks help identify conserved genomic regions between species
- Use in combination with gene tracks to find orthologous gene regions
- Color coding makes it easy to identify which chromosome in the target species corresponds to the displayed region
- Arrow direction indicates whether gene order is preserved or inverted between species
