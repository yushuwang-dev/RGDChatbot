---
source_url: https://rgd.mcw.edu/wg/help3/tools/pm2-0/
tool_url: https://rgd.mcw.edu/rgdweb/phenominer/home.html
---

# RGD PhenoMiner Help

## Overview

PhenoMiner is a tool for ontology-based storage and analysis of quantitative phenotype data specific to laboratory rats. The system incorporates data from both high-throughput phenotyping initiatives (standardized) and scientific literature sources (unstandardized).

## Core Ontological Framework

The system uses four primary ontologies to enable comparative analysis and flexible querying:

1. **Clinical Measurement Ontology** - Defines what measurements were taken
2. **Measurement Method Ontology** - Specifies how measurements were conducted
3. **Experimental Condition Ontology** - Describes measurement conditions
4. **Rat Strain Ontology** - Identifies animal subjects

The **Vertebrate Trait Ontology** groups related measurements within studies.

## Accessing PhenoMiner

Access PhenoMiner through the "Analysis & Visualization" menu section on RGD pages, or directly from the Phenotypes & Models section.

## PhenoMiner 2.0 Interface

### Single-Page Design

The system consolidates all components on one interface. The Strain Ontology loads automatically, though users can begin with any ontology via tabs in the lower right panel.

### Key Interface Elements
- Selections made in bottom panels appear in top display boxes
- Left panel includes a search function and alphabetically-organized term listings with associated PhenoMiner records
- Search narrows available terms instantly
- "Select" option places terms in top boxes and expands corresponding ontology tree sections for refinement

## Selection and Modification

- All selections occur within the same screen with immediate visual feedback
- Toggle between ontologies using bottom right panel tabs
- Options dynamically adjust based on prior selections
- **"Generate Report"** button initiates analysis from selected parameters
- Term removal uses checkboxes in lower panels or X buttons in top displays

## Results Display

The results interface comprises three interconnected components:

### 1. Graph
Visual representation of quantitative data.

**Important:** If measurements that use more than one unit have been selected, the graph is hidden until the user filters the measurement selection.

### 2. Filter List
Left-side limiting options for narrowing results by strain or other criteria.

### 3. Results Table
Detailed data records with sortable columns.

### Filter Interactions
Filters, graphs, and tables communicate bidirectionally. Users search for strains via search boxes or lower section options.

## Graph Features

### "Colored by" Function
A dropdown above the graph enables users to select coloring parameters for bar visualization. The legend dropdown clarifies color-to-measurement correspondence.

### Data Download
- "Download all records" button for both filtered and unfiltered queries
- Filtered queries additionally offer table-view-only download options

## Table Sorting and Graph Reordering

Column headers display directional arrows indicating sortable fields. Sorting the table reorders the bars in the graph accordingly.

## Individual Animal Data

When individual rat measurements are submitted, the graph displays both averaged values and individual data points.

- **Red dots** indicate individual animal values within bars
- **Hovering over bars** reveals average sample values and conditions
- **Hovering over dots** displays specific individual rat measurements
