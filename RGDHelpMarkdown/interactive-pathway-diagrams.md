---
source_url: https://rgd.mcw.edu/wg/help3/data/interactive-pathway-diagram-report-page-hel
---

# RGD Interactive Pathway Diagram Report Pages

## Overview

The updated interactive pathway diagram report pages offer increased informational content and navigational capabilities. Each pathway report page functions as a mini-portal with multiple interconnected sections.

## Report Page Sections

### Description Section
The pathway title appears with its Pathway Ontology term in parentheses, linked to the ontology report page. Descriptions are expandable - click "(more)" for full text or "(less)" to collapse. The section includes links to associated GO terms, KEGG, and Reactome databases where applicable. Protein domains mentioned link to Pfam database entries.

### Pathway Diagram Section
Diagrams are created using Ariadne Genomics Pathway Studio software (version 8.0), incorporating mammalian ResNet Database data on rat, mouse, and human genes, diseases, and molecules. RGD's parser identifies properties like RGD:ID, enabling links to gene and pathway report pages, ontology pages, and external databases. Shapes represent specific functionalities (kinase, phosphatase, transcription factor, etc.).

### Go To Section
A table listing accessible entries in tabular form. Clicking entries takes users directly to their report page locations. Current entries include:
- Genes
- Additional Elements
- Disease Annotations to Pathway Genes
- Pathway Annotations to Pathway Genes
- Ontology Path Diagram

Altered pathway versions with annotations appear here when available.

### Genes in Pathways Section
Gene annotations display by species in sortable tables (default: rat genes; options for mouse and human). Tables provide:
- Chromosome positions
- Start/stop coordinates
- JBrowse links
- Reference information

The "A" icon links to comprehensive gene annotations across all RGD ontologies. Users can toggle "show annotations for term's descendants" to filter results. A tree icon accesses ontology term hierarchy views.

### Additional Elements Section
Other pathway components - including pathways, small molecules, gene groups, complexes, and functional classes - appear with descriptions and applicable links. Objects representing the same gene under different functional states or locations are distinctly labeled (e.g., "diss-Irak1" for dissociated protein, "cytTraf6" for cytoplasm-translocated protein).

### Disease Annotations Section
Rat gene disease annotations display in togglable tabular formats:
- **Default view** - Diseases alphabetically (left column) with associated genes (right)
- **"Genes/Disease" tab** - Lists genes alphabetically with their disease annotations

Clicking diseases accesses relevant ontology reports.

### Pathway Annotations Section
Similar to disease annotations:
- **Default view** - Pathways alphabetically with associated genes
- **"Genes/Pathways" tab** - Lists genes with their pathway annotations

Clicking pathways accesses corresponding ontology reports.

### References Section
All PubMed references associated with the pathway. Clicking references opens the reference report with PubMed links. Green plus signs reveal associated pathways and annotated objects.

### Ontology Path Diagram Section
Displays the hierarchical path(s) from the term to the pathway ontology root. The term itself appears highlighted in darker shading. Clicking the term or parent terms accesses their ontology report pages.

### Import into Pathway Studio
Located beneath the Ontology Path Diagram, this feature allows users with Ariadne's Pathway Studio package to import the .gpp file for local analysis.
