---
source_url: https://rgd.mcw.edu/wg/help3/ontology-report-annotations-help-page/
---

# RGD Ontology Report - Annotations Help

## Overview

The Ontology Report - Annotations page contains information about ontology terms and linked annotated objects. It is organized into five primary sections:

1. **Term Information** - Details about the selected term
2. **Genome Viewer (GViewer)** - Chromosome ideogram display
3. **Gene Table** - Annotated genes, QTLs, and strains
4. **Ontology Lineage** - Tree and DAG displays
5. **Evidence Codes** - Reference guide

## Term Display Information

The term appears at the top with associated metadata:
- **Accession** - Can be used for general ontology searches to locate exact terms
- **Definition** - Explains the term's meaning
- **Synonyms** - Include alternate names previously used or identifiers from different communities

### Navigation Features
- **Search Field** - Enables general ontology searches from within the page
- **Main Ontology Link** - Navigates back to the primary ontology search page
- **Browse Link** - The green branch icon links to the ontology browser
- **Alliance Link** - Provides access to term-specific information at the Alliance of Genome Resources

## Genome Viewer (GViewer)

The GViewer diagram is a fully functional copy embedded directly in the Ontology Report.

### Chromosome Ideogram
Displays genomic positions of all rat genetic objects annotated with the ontology term.

### Object Color Coding
- **Genes** - Dark red
- **QTLs** - Blue
- **Congenic strain regions** - Green (displayed to the right of each chromosome)

### Zoom Functionality
Clicking a chromosome opens a zoom pane for closer examination. A second click locks the slider. Object symbols in the zoom pane link to report pages.

### Toolbar Features
- **List All Objects** - Opens a popup listing all diagram objects ordered by chromosome
- **CSV Export** - Download options for all objects, shared objects, or unique objects
- **Add Objects** - Overlay additional gene, QTL, strain, or ontology term annotations with custom colors
- **Send to JBrowse** - Navigate to JBrowse genome browser for the selected region

## Annotation Term Browser

Below the Genome Viewer is a table displaying all objects annotated to the selected term and descendant terms.

### Sorting Options
- **Checkbox** (default selected) - Displays information for all descendant terms plus selected term. Deselect to view only the selected term's annotations
- **Sort dropdown 1** - Options: symbol, object name, position, or reference
- **Sort dropdown 2** - Ascending or descending order

### Download
Export terms, associated objects, and annotation information to a text file.

### Species and Object Tabs
- **Species tabs** - Rat, Mouse, Human, Chinchilla, Bonobo, Dog, Squirrel, Pig, or All (with annotation counts)
- **Object tabs** - Genes, QTLs, or Strains (with annotation counts for selected species)

### Symbol Color Coding
- Dark red "G" - Gene
- Blue "Q" - QTL
- Green "S" - Strain

### Evidence Code Links
Selecting an evidence code opens the gene-term annotation report viewable as list (default) or table.

### External Source Data
Links to sources like ClinVar, OMIM, CTD providing additional information.

### References
Select PubMed links to access manuscripts. RGD references link to publication pages with associated annotation information.

## Ontology Term Lineage

### Tree Format
- Presents lineage from highest-level root term to selected term's direct children
- Purple boxes represent relationships between terms (hover to see relationship description)
- Plus signs show number of descendant terms for child terms
- Annotations column shows annotation count for term and all descendants

### Directed Acyclic Graph
- Presents term lineage and relationship pathways from child terms through parent terms to root term
- Yellow boxes are selectable to reach associated ontology report pages
- Dropdown menu controls graph display format
