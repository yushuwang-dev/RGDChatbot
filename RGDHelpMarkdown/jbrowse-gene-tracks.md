---
source_url: https://rgd.mcw.edu/wg/help3/tools/rgd-genome-browsers/the-rat-jbrowse-genome-browser/more-about-jbrowse-tracks/rgd-gene-related-tracks
tool_url: https://rgd.mcw.edu/jbrowse/
---

# RGD JBrowse Gene-related Tracks

## Overview

Gene-related tracks are available in JBrowse across various RGD genome assemblies (rat, mouse, and human). At least three standard RGD gene feature tracks are available, plus disease-related and gene-chemical interaction tracks.

## RGD Genes and RGD Genes and Transcripts Tracks

### Gene Tracks
The "Gene" tracks represent each gene as a rectangular box covering the entire region spanned by any transcript. For example, if transcript one spans positions 100-1500 and transcript two spans 150-3000, the gene box displays as 100-3000.

### Genes and Transcripts Track
Displays individual transcripts assigned to each gene, with NCBI RefSeq IDs shown to the left of each transcript and the gene symbol displayed below the transcript cluster.

### Interaction Features
- Mousing over highlights the entire group and displays a tooltip with the gene symbol
- Useful when zoomed in to show only part of a gene
- Clicking the gene glyph opens an "RGD Feature Data" popup

### Popup Information
- Gene symbol and name
- Gene type
- NCBI RefSeq status
- Species information
- Description
- External database identifiers (linked to corresponding databases)
- Location link (zooms to display entire gene)
- "RGD Gene Annotation Analysis" link (opens Gene Annotator Tool)
- Links to Ensembl, NCBI Gene, UniGene, and UniProt records

## RGD Transcript Tracks

Focuses on individual transcripts rather than genes. Transcripts are not clustered by gene assignment. Each transcript displays as a "line and box" glyph showing introns (lines) and exons (boxes), with the RefSeq ID shown below.

### Popup Information
- Transcript class (e.g., mRNA)
- Genomic location and length
- Associated gene
- Transcript-specific RefSeq status
- Protein-coding designation
- Transcript ID link to GenBank record at NCBI

## RGD Ontology-based Gene Tracks

### Disease Related Tracks
- Based on RGD annotations to Disease ontology terms
- Organized by disease categories (highest-level terms) such as "Cardiovascular Diseases" and "Endocrine System Diseases"
- Data imported from databases like OMIM and ClinVar

**Disease Track Popup includes:**
- General gene information (location, symbol, name, type, descriptions)
- List of all disease ontology terms within that category associated with the gene
- RDO IDs linking to RGD ontology reports

### Gene-Chemical Interaction Tracks
- Based on "Biological Role" branch of ChEBI (Chemical Entities of Biological Interest) vocabulary
- Display genes interacting with chemicals of specific roles

**Popup includes:**
- Chemical name (links to RGD ontology report)
- Phrase describing interaction type
- Links to RGD Gene-chemical interactions report
- "Multiple interactions" designation for complex relationships

## Gene-related Histogram Displays

As users zoom out over large chromosomal regions:
1. Individual gene labels disappear
2. Gene glyphs stack vertically
3. At approximately 10-30 Mb display levels, JBrowse converts to "feature density" histograms
4. The tool divides displayed regions into subregions, counts features, and displays as histograms

**Note:** The RGD Transcripts histogram differs from gene-based histograms since transcripts are counted individually.

## RNA-Seq Gene Prediction Tracks

Displays researcher-submitted RNA-Seq data showing predicted intron/exon structures. Available under "Gene Models > RNA-Seq Predicted Gene Models."

**Important notes:**
- Absence of a gene prediction does not prove lack of expression in that tissue
- Poor sequencing quality or quantity may prevent gene prediction
- Predicted transcript names are researcher-assigned identifiers, not necessarily known gene names

**Reference:** "Improved rat genome gene prediction by integration of ESTs with RNA-Seq information." Li et al, Bioinformatics. 2015 Jan 1;31(1):25-32. PMID: 25217576
