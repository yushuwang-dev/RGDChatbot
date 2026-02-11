---
source_url: https://rgd.mcw.edu/wg/help3/marker-report-help-page/
---

# RGD Marker Report Page Help

## Overview

This guide helps users understand RGD marker report pages. Users can access these reports via the Marker Search Tool or by entering a marker symbol in the General Search bar.

## General Section

The marker report displays species information with a navigable outline on the left sidebar allowing users to jump between sections.

General information includes:
- Marker symbol, alias, and RGD ID
- Expected PCR product size
- Chromosome and position locations with sources

Clicking on the assembly in the JBrowse column opens a JBrowse interactive page for that marker location.

Associated data presented as clickable links:
- Strains
- QTLs
- Genes

**Note:** RGD does not manually assign ontology annotations to Markers, but references are given for the marker information displayed.

References include curated associations, imported data sources, and published mapping papers.

## Strains and Sequence Section

### Marker Types

A marker which is a simple sequence length polymorphism (SSLP) is defined by the PCR primer pair used to amplify and visualize the segment of DNA containing the polymorphism.

RGD stores data for:
- SSLPs (Simple Sequence Length Polymorphisms)
- ESTs (Expressed Sequence Tags)
- SNPs (Single Nucleotide Polymorphisms)
- Other marker types (may or may not have primer pairs)

### Strain Variation

Many SSLPs are polymorphic in size among rat strains due to differing numbers of short nucleotide repeats within the SSLP sequence.

The Strain Variation section lists nucleotide sizes with corresponding strain/substrain symbols. Strain names are clickable links to strain report pages.

## Region Section

Contains:
- Information about genes and other data objects in the SSLP's genomic neighborhood
- Links to GenBank nucleotide sequences of the SSLP

## QTL Section

### QTLs in Region

Provides a table of QTLs and genes overlapping the SSLP position.

**Menu Options:**
- **Full Report** - Links to the interactive QTL search page
- **CSV** - Download list in comma separated values format
- **TAB** - Download list in tab delimited format
- **Printer** - Sends list to default printer
- **GViewer** - Sends list to genome-wide viewer tool

The QTL table provides columns of information about each QTL as noted in the column names. For detailed QTL information, refer to the QTL report help pages.

## Additional Information Section

### Data Sources

RGD imported marker data from UniSTS until NCBI discontinued the database. In addition, marker information is curated from the literature and received directly from researcher submissions.

### External Database Links

Data is displayed in the External Database Links section, whether automatically imported or manually entered. Links may include NCBI Gene references for genes and QTLs. Clicking the accession ID takes the user to the corresponding record at the external database.
