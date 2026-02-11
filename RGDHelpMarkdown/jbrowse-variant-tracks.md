---
source_url: https://rgd.mcw.edu/wg/help3/tools/rgd-genome-browsers/the-rat-jbrowse-genome-browser/more-about-jbrowse-tracks/variant-tracks
tool_url: https://rgd.mcw.edu/jbrowse/
---

# RGD JBrowse Variant Tracks

## Overview

The Rat Genome Database stores and presents several categories of variant data. Researchers performing whole genome sequencing on rat strains submit variant calls to RGD, which are then loaded into the Variant Visualizer tool and genome browsers. The database also imports single nucleotide variation (SNV) and simple sequence length polymorphism/microsatellite marker (SSLP) data from NCBI and Ensembl.

## Strain Specific Variant Tracks

Most strain-specific variant tracks display single nucleotide variants (SNVs); some JBrowse instances include indel tracks as well.

### Accessing Strain Variants
1. Select "Variants" in the "Available Tracks" list
2. Choose "Strain Specific Variants"
3. Select desired strains

Strains are listed with their symbol followed by an institutional abbreviation (e.g., "WKY/N (KNAW)" and "ACI/Eur (MCW)"). Different substrains of the same strain may be sequenced, enabling comparisons.

### Variant Popup Information
- **Strain** - Symbol and institutional abbreviation
- **Position** - Chromosome number and nucleotide position
- **Reference Nucleotide** - The nucleotide in the reference sequence
- **Variant Nucleotide** - The predicted nucleotide(s) at that position
- **Location** - Either "GENIC" (overlaps gene position) or "INTERGENIC"
- **Zygosity** - Heterozygous, Homozygous, or Possibly Homozygous
- **Related Variants** - RS ID if the variant appears in dbSNP
- **Conservation** - Conservation score (0-1) from UCSC database, or "n/a"
- **Total Depth** - Read depth at that position
- **% Variant Reads** - Ratio of variant reads to total reads x 100
- **Total Alleles Read** - Number of different nucleotide assignments at that position
- **VID** - Unique variant ID assigned by RGD

### Transcript Information (for genic variants)
- **Accession** - RefSeq accession number of transcript mRNA/cDNA
- **Location** - Where the variant occurs (INTRON, EXON, 5UTR, etc.)

### For protein-coding exons
- **Amino Acid Prediction** - Shows the amino acid change (e.g., "I to I (synonymous)" or "V to I (nonsynonymous)")
- **Polyphen Predictions** - Available predictions of non-synonymous amino acid change consequences
- **Amino Acid Sequence** - The calculated protein sequence with the affected amino acid in bold red

**Note:** Since variants are called relative to genomic reference sequences, informatically translated protein sequences may not match published sequences from RefSeq or UniProt. Warning messages appear when stop codons are found in the middle of putative peptide sequences.

## Indel Tracks

The RGSC v3.4 JBrowse includes strain-specific indel tracks. "Indel" denotes insertions, deletions, or combinations thereof resulting in net nucleotide changes relative to the reference sequence (1-few hundred nucleotides).

### Display Characteristics
- At zoomed-out views: indels appear as vertical lines
- At higher zoom (approximately 200 nucleotides or less):
  - **Deletions** - Red bars covering the deleted nucleotide count
  - **Insertions** - Blue bars one nucleotide long, marking the insertion position

### Indel Popup Information
- **Source** - Strain and analysis group/institution
- **Class** - "INDEL"
- **Genome Location** - Chr:Start..Stop
- **Feature Length** - Deletion length or one base pair for insertions
- **Variant ID** - First inserted/deleted base pair position plus notation
- **Variant type** - Insertion or deletion
- **Reference** - Sequence of reference allele
- **Strain** - The sequenced strain symbol
- **Filtered depth** - Sequence depth after quality control
- **Variant call analysis** - Variant sequence and read count

## dbSNP and Ensembl Variant Tracks

RGD imports variant data from both NCBI (dbSNP) and Ensembl. Variants are represented as vertical line glyphs; zoom to under approximately 200 bp to see wider bars. Both are color-coded according to variant type following Sequence Ontology (SO) classifications.

### dbSNP Popup Information
- **Source** - Data origin
- **Class** - Variant type (typically "SNP")
- **Genome Location** - Chr:Start..Stop
- **Feature Length** - Base pair length (1 bp for SNPs)
- **ID** - RS (Reference SNP) ID
- **Accession** - Unique RGD identifier
- **Map Weight** - How many times the variant maps to a contig
- **Type** - Transcript-level location or coding change type
- **Allele** - reference_nucleotide/variant_nucleotide

### Ensembl Popup Information
- **Source** - Data origin
- **Class** - Variant type
- **Genome Location** - Chr:Start..Stop
- **Feature Length** - Base pair length
- **ID** - Unique identifier (often RS ID)
- **Strain(s)** - Symbol and RGD ID of strains containing the variant
- **Map Weight** - Mapping frequency
- **Type** - Transcript-level location or coding change
- **Allele** - reference_nucleotide/variant_nucleotide

## Marker/SSLP Tracks

SSLPs (Simple Sequence Length Polymorphisms) are 1-6 simple nucleotide repeat sequences which are polymorphic in length among strains or between individuals. Each SSLP in RGD is defined by PCR primer sequences.

### Display Characteristics
- Appear as vertical lines until zoomed in enough to show dark green horizontal bars
- At regions greater than 45 Mb, display changes to marker density histograms
- Label format: "SSLP:Marker_Symbol"

### Marker/SSLP Popup Information
- **Source** - "RGD"
- **Class** - "SSLPS"
- **Genome Location** - Chr:Start..Stop (based on ePCR primer positions)
- **Feature Length** - Region from forward primer to reverse primer
- **Name** - Official marker symbol
- **RGD Marker Report** - RGD ID linking to the marker report
- **Expected Size** - Original marker size (may differ from feature length due to assembly or strain differences)
