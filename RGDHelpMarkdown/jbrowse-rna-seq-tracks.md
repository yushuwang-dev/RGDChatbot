---
source_url: https://rgd.mcw.edu/wg/help3/tools/rgd-genome-browsers/the-rat-jbrowse-genome-browser/more-about-jbrowse-tracks/rna-seq-based-tracks
tool_url: https://rgd.mcw.edu/jbrowse/
---

# RGD JBrowse RNA-Seq Based Tracks

## Overview

JBrowse introduces RNA-Seq data into RGD's genome browsers. Researchers can submit BAM alignment files showing RNA-Seq reads aligned to the RGSC5.0 reference genome. The system currently hosts data including a Lazar BN-SS Hypoxia-Normoxia Study and gene predictions from the Liu lab based on RNA-Seq data from bone marrow, brain, and kidney tissues.

## BAM Alignment Display

JBrowse displays short next-generation sequencing reads aligned to the reference genome using color-coding:

| Color | Meaning |
|-------|---------|
| Light Red (#EC8B8B) | Forward strand, mate pair present |
| Light Blue (#898FD8) | Reverse strand, mate pair present |
| Dark Red (#D11919) | Mate pair absent |

Black lines between blocks indicate gapped alignments, often corresponding to splice junctions where RNA sequence segments align at different locations.

## Context-Specific Menu Options

Right-click menu for BAM tracks includes:

- Hide PCR/optical duplicate reads (default: hidden)
- Hide reads failing vendor quality control (default: hidden)
- Hide reads with missing mate pairs (default: shown, color-coded)
- Hide secondary alignments (default: hidden)
- Hide supplementary alignments (default: hidden)
- Hide forward strand reads (default: shown)
- Hide reverse strand reads (default: shown)

## BAM Alignment Popup Information

Clicking a segment displays detailed metadata including:

### Mapping Data
- Name, type, mapping quality score
- Genomic position with strand designation

### Sequence Details
- Nucleotide sequence with quality scores (-10 log10 probability of error)

### Alignment Metrics
- **AS** - Alignment score
- **CIGAR** - Matched/skipped sequence notation
- **MD** - Mismatch positions
- **MQ** - Mapping quality
- **NH** - Number of reported alignments
- **NM** - Edit distance
- User-defined tags (XG, XM, XN, XO, XS, YT)

### Quality Flags
- QC pass/fail status
- Secondary/supplementary alignment designation
- Unmapped status
- Sequence reverse complementation

### Source Information
- BAM filename origin and sequence length

## Track Height Adjustment

High-expression regions produce massive read counts, often displaying "Max height reached" warnings. To adjust:

1. Open the context-specific menu
2. Select "Edit config"
3. Find the fourth line: `"maxHeight": 600,`
4. Change the number (e.g., to 1200)
5. Preserve the comma

## Histogram Display

When zoomed out beyond approximately 20 kilobases, individual alignments convert to histograms showing read density on a logarithmic scale.

- Histogram height = log2(read count + 1 offset)
- Formula: `numReadsAligned = 2^(histogramHeight - 1)`
- Height of 10 = approximately 512 aligned reads
- Maximum value 16 = approximately 65,000 reads per segment

## RNA-Seq Gene Prediction Tracks

Available under "Gene Models > RNA-Seq Predicted Gene Models > Cancer Center, Medical College of Wisconsin."

These tracks show predicted intron/exon structures from RNA-Seq data from bone marrow, brain, and kidney (with and without EST data).

### Important Notes
- Absence of a gene prediction does **not** prove lack of expression in that tissue
- Poor sequencing quality or quantity may prevent gene prediction
- Predicted transcript names are researcher-assigned identifiers, not necessarily known gene names

### Popup Information
- Source (tissue and method)
- Genomic location links
- Predicted gene/transcript length
- Researcher-assigned names
- Load ID and Primary ID

**Reference:** "Improved rat genome gene prediction by integration of ESTs with RNA-Seq information." Li et al, Bioinformatics. 2015 Jan 1;31(1):25-32. PMID: 25217576
