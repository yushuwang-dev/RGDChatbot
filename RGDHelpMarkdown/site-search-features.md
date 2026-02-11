---
source_url: https://rgd.mcw.edu/wg/help3/tools/site-search
tool_url: https://rgd.mcw.edu/rgdweb/search/search.html
---

---
source_url: https://rgd.mcw.edu/wg/help3/tools/site-search
tool_url: https://rgd.mcw.edu/rgdweb/search/search.html
---

# RGD Site Search Features

## Overview

RGD site search allows users to find objects based on keyword or position information. Over 8.5 million terms are indexed to return Genes, QTLs, Strains, Markers, References, and Ontology terms.

**Basic Usage:** Type search terms into the search box and click "Search RGD."

## Key Search Features

### Capitalization

Searching is **not case sensitive**. "BLOOD PRESSURE," "blood pressure," and "BlOoD PrEsSuRe" all return identical results.

### Automatic "AND" Queries

RGD returns only objects indexed against **all** search terms entered. Searching "blood pressure" returns items containing both words; items with only one term are excluded.

### Searching by RGD ID

Enter an integer alone to search by RGD ID. For example, entering **2004** retrieves the A2m gene page.

### External Identifiers

Over 4 million external identifiers are indexed. Prefix numeric searches with a colon (**:**) to search identifiers rather than RGD IDs. Non-numeric searches automatically attempt external identifier matching. Examples include PubMed and Entrez Gene IDs.

### Common Word Exclusion

RGD automatically excludes common words like "is" and "then," plus single characters.

### Phrase Searches

Use quotation marks for exact phrases. Searching **"hypertensive strain"** returns only objects containing that exact phrase with single-space separation.

### Negative Terms

Add a minus sign to exclude terms. **blood -pressure** returns blood-related objects excluding pressure references.

### Positional Searching

Search by genomic position using format: **chr2:12000000..130000000** returns objects on chromosome 2 between specified base pairs.

### Object Families / Word Variations

Default searches include trailing wildcards. Searching **lepr** retrieves all terms beginning with "lepr."

### Wildcards Within Terms

Insert asterisks for mid-term wildcards. When asterisks are present, automatic trailing wildcards are disabled.

## Indexed Content (8.5+ Million Terms)

### Gene Information
- Symbols
- Descriptions
- Names
- Aliases

### QTL Data
- Traits
- Sub-Traits

### Strain Data
- Origins
- Sources

### References
- Titles
- Citations

### Ontology Terms
- Gene Ontology (GO)
- Pathway Ontology
- Mammalian Phenotype Ontology
- Disease Ontology

### External Database Identifiers

The following external databases are indexed:

BIND, Ensembl (Genes/Protein/Transcript), Entrez Gene, GenBank (Nucleotide/Protein), Gene3D-CATH, Germonline, HGNC, HPRD, HomoloGene, IMAGE_CLONE, IPI, InterPro, KEGG (Pathway/Report), MGC_CLONE, MGD, NCBI Nucleotide, OMIM, PANTHER, PIRSF, PRINTS, PROSITE, Pfam, PharmGKB, ProDom, PubMed, SMART, Superfamily-SCOP, TIGR, TIGRFAMs, Transposagen, UniGene, UniProtKB, UniSTS
