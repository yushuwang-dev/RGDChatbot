---
source_url: https://rgd.mcw.edu/wg/help3/tools/rgd-genome-browsers/the-rat-jbrowse-genome-browser/more-about-jbrowse-tracks/rgd-qtl-and-strain-tracks
tool_url: https://rgd.mcw.edu/jbrowse/
---

# RGD JBrowse QTL and Strain Tracks

## Overview

JBrowse includes tracks for both Quantitative Trait Loci (QTLs) and congenic strains. A QTL is a physical chromosomal location containing one or more alleles that differentially affect the expression of a continuously distributed phenotypic trait such as blood pressure, body weight, etc.

## RGD QTLs Track

### Visual Representation
QTLs appear as horizontal **blue "box glyphs"** in JBrowse, distinguishing them from red gene tracks and green strain tracks. The average rat QTL size is 45 Mb. Some chromosomal regions contain 80-90 overlapping QTLs.

### Navigation
- QTL symbols display beneath the 5' end
- Mouse over QTLs to reveal symbols
- Click for detailed popup information

### QTL Popup Information
- **Source:** RGD
- **Class:** QTL
- **Genome Location:** Chr#:startPosition..stopPosition (links to full JBrowse region)
- **Feature Length:** Genomic length on corresponding assembly
- **Name:** Official QTL symbol
- **Full Name:** Official complete designation

### QTL Positioning Methods

Positions derive from flanking and/or peak marker locations via RGD's automated pipeline:

1. **Positioned by flanking markers** - Both upstream and downstream markers available. QTL extends from 5' of upstream to 3' of downstream marker. Takes precedence over peak marker.

2. **Positioned by flanking marker and peak marker** - Single flanking marker plus peak marker used when all three aren't available. QTL centered on peak marker.

3. **Positioned by peak marker only** - Default QTL length assigned: 45 Mbp (rat), 34 Mbp (mouse), 26 Mbp (human), centered on peak.

4. **Positioned by single flanking marker only** - QTL extends from available marker with default species average length.

5. **Position imported from external source** - Data from outside sources (e.g., Mouse Genome Database).

### Statistical Measures
- **LOD** (Logarithm of Odds) - Log ratio of QTL presence vs absence. Higher scores = greater statistical significance.
- **P-value** - Association significance, often genome-wide adjusted.

### Additional Popup Fields
- **RGD ID** - Links to complete RGD report page
- **Related QTLs** - Researcher-indicated relationships (sub_region, maps to same region, interacts with, maps to syntenic region)
- **Related Strains** - Strains crossed to derive the QTL
- **Candidate Genes** - Researcher-suggested genes contributing to the phenotype
- **Gene Annotation Analysis** - Link to Gene Annotator Tool

## RGD Congenic Strains Track

### Visual Representation
Congenic strains appear as horizontal **green "box glyphs"** in JBrowse. Symbols display beneath the 5' end.

### Strain Popup Information
- **Source:** Original development institution
- **Class:** Strain type
- **Genome Location:** Full introgressed region coordinates
- **Feature Length:** Introgressed region length in base pairs
- **RGD Rat Strain:** Official strain symbol
- **Phenotype Ontologies:** Demonstrated strain phenotypes with Mammalian Phenotype Ontology IDs
- **Disease Ontologies:** Diseases that strains model or recapitulate
- **Description:** Brief strain derivation summary

### Full Region Display
Strain popups provide links to full introgressed region coverage in JBrowse. Unlike QTL and gene tracks that convert to histograms at large zoom levels, congenic strain regions display individually across entire chromosomes due to lower numerical density.

## Color Coding Summary

| Object Type | Color |
|------------|-------|
| Genes | Red |
| QTLs | Blue |
| Congenic Strains | Green |
