---
source_url: https://rgd.mcw.edu/wg/help3/qtlhelp/
tool_url: https://rgd.mcw.edu/rgdweb/search/qtls.html
---

# RGD QTL Help

## What is a QTL?

A **Quantitative Trait Locus (QTL)** is a physical chromosomal location containing one or more alleles that differentially affect the expression of a continuously distributed phenotypic trait such as blood pressure, body weight, etc. It typically represents an area delineated by strain-specific markers. When genetic variation in the locus shows statistical association with measured trait variation, a QTL results.

## How QTLs Are Identified

Disease-specific QTLs in rat models derive from genetic crossing and analysis:

1. An affected strain (showing the phenotype) is crossed with an unaffected strain
2. Progeny are genotyped and phenotyped
3. Statistical techniques are used to correlate specific genotypes with measured phenotypes
4. QTLs are expected to contain one to many genetic elements contributing to the phenotype

## QTL Data in RGD

RGD curates rat and human QTLs and imports mouse QTLs from Mouse Genome Informatics (MGI).

For a comprehensive review of QTL mapping techniques, see: "Genetic Analysis of Inherited Hypertension in the Rat" by John Rapp, *Physiological Reviews*, 90:135-172, 2000.

## Searching for QTLs

### RGD Search Method
The search function queries QTL symbols, names, aliases, trait names, trait description/method, and annotations.

**Quick Guide:**
1. Access the QTL search page from the RGD home page under "Data"
2. Enter search terms in the search box
3. Click search
4. Alternatively, enter search terms in the upper right search box from any RGD page

### QTL Search Page
1. Access directly from the RGD home page under "Data"
2. Enter the QTL symbol/keyword and click "Search QTLs"
3. Available options include rat, human, and mouse species selection, plus chromosome position search
4. Search results display available QTLs matching the search term
5. Users can click on Genome Viewer (GViewer) to view genomic positions or download results using Excel Download

## QTL Report Page

### General Tab

The "General" tab contains primary RGD information about the QTL:

- **Symbol** - The approved QTL symbol (may differ from symbols used in articles; all alternative symbols appear in the alias section)
- **Name** - The approved full-text name and number of the QTL
- **Trait** - The measurable phenotypic trait using Vertebrate Trait ontology terms mapped to the QTL. When multiple traits are reported, only the highest statistical significance trait appears
- **Measurement type** - How the trait was measured using Clinical Measurement Ontology terms
- **LOD Score** - Logarithm of the odds score indicating linkage significance between two loci or between a locus and a phenotype/disease
- **P value** - The probability of obtaining a test statistic as extreme as observed, assuming the null hypothesis is true
- **Variance** - A measure of variability in a set of numbers
- **Position** - Chromosome and map coordinate positions for the QTL in different genome assemblies (five assemblies shown), with source information
- **Cross Type** - The cross type used to determine the QTL
- **Strains Crossed** - The strains used to determine the QTL (strain symbols link to Strain reports)
- **JBrowse** - View QTL position in the genome browser

### Icon Features

- **Branch Icon** - Opens the ontology browser page displaying parent, sibling, or child terms, synonyms, and graphical term relationship structures
- **Annotation Icon** - Directs to the ontology annotations report page showing all objects associated with the term

## Annotations Section

### Disease Annotations
Disease-to-QTL associations manually curated from biomedical literature or imported through automated pipelines from OMIM (Online Mendelian Inheritance in Man) or GAD (Genetic Association Database). Terms derive from the RGD Disease Ontology (RDO), which combines RGD-created disease terms with the Disease Ontology.

### Phenotype Annotations
QTL associations with particular phenotypes using terms from the Mammalian Phenotype Ontology (MP) developed at MGI, and the Human Phenotype Ontology (HPO) currently developed at the Jackson Laboratory for Genomic Medicine.

### Experimental Data Annotations
Annotations using terms from five different ontologies with appropriate evidence codes, curated from papers originally describing the QTL. Each term links to a Term Annotation Report.

### Annotation Summary View
Clicking "Click to see Annotation Summary View" displays annotations in summary mode showing the measurable phenotypic trait mapped to the QTL.

## References - Curated

All references connected to annotations on the QTL report page are listed. Citations link to RGD Reference report pages, which typically link to PubMed.

## Region Section

### Genes in Region
Lists genes in the genome assembly overlapping the QTL region with descriptive information. Data is downloadable and exportable to analysis tools.

### Markers in Region
Lists markers overlapping the QTL region. Data is downloadable, exportable, and viewable in GViewer.

### GViewer Position Markers
Lists flanking and/or peak markers with positional and source information and links to marker report pages.

### QTLs in Region
Lists other QTLs overlapping the QTL region. Data is downloadable and exportable.

## Additional Information

### RGD Curation Notes
Descriptive curator notes in several categories are listed with reference links.
