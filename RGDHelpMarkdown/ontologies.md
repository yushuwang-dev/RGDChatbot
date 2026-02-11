---
source_url: https://rgd.mcw.edu/wg/help3/data/ontologies
---

# RGD Ontologies Help

## What is an Ontology?

Ontologies in biomedical contexts are controlled vocabularies in which a set of related concepts and ideas that are relevant to a field are organized in a hierarchical fashion, similar to an outline. General concepts are placed at higher levels and specific concepts are assigned to lower levels.

### Example: Protein Ontology Hierarchy
- Top level: Protein
- Secondary level: Enzyme, Structural Proteins, Binding Protein
- Lower levels: Kinase, Polymerase, Isomerase, Transferase, Protease, Collagen, Keratin, DNA-binding Protein, RNA-binding Protein

## Key Ontology Features

### Relationships Between Concepts
- **"is_a" relationship** - Represents hierarchical classification (kinase is a type of enzyme)
- **"part_of" relationship** - Represents composition (stomach is part of digestive system)

### Multiple Parents and Children
Concepts can have multiple parents and children, creating a Directed Acyclic Graph (DAG) structure. This allows complex knowledge representation while maintaining hierarchy specificity and preventing circular relationships.

### Ontologies as Knowledge Bases
Typically, specific examples or instances are linked (annotated) to the concepts. An ontology with annotations is called a knowledge base.

## RGD Implementation

RGD uses ontologies to provide new avenues by which users can find and focus on object information. Currently, RGD uses the Gene Ontology plus fifteen additional ontologies, applied to genes, quantitative trait loci, strain objects, and general search keywords.

### Ontologies Used in RGD

1. **Gene Ontology (GO)** - First implemented at RGD; covers biological process, cellular component, and molecular function
2. **Disease Ontology / RGD Disease Ontology** - Hybrid of Disease Ontology and RGD-created disease terms
3. **Pathway Ontology** - Biological pathway classifications
4. **Clinical Measurement Ontology** - Defines what measurements were taken
5. **Measurement Method Ontology** - Specifies how measurements were conducted
6. **Experimental Condition Ontology** - Describes measurement conditions
7. **Rat Strain Ontology** - Classifies rat strains
8. **Chemical Entities of Biological Interest (ChEBI)** - Chemical compound classifications
9. **Mammalian Phenotype Ontology** - Phenotype descriptions for mammals
10. **Human Phenotype Ontology** - Human-specific phenotype descriptions
11. **Vertebrate Trait Ontology** - Created collaboratively with MGI and Animal QTL database

These ontologies standardize curated data and enable organized presentation to users.
