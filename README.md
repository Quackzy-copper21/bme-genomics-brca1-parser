# NCBI BRCA1 mRNA Sequence Analysis & Visualisation

## Overview
This repository contains a computational biology pipeline written in Python to fetch, parse, and analyze the raw mRNA transcript sequence of the human *BRCA1* (BReast CAncer gene 1) gene sourced from the NCBI / NIH database.

## Biological Context
*BRCA1* is a critical tumor suppressor gene located on human chromosome 17. It plays a primary role in genomic stability and DNA double-strand break repair via homologous recombination. Pathegonic mutations in *BRCA1* significantly increase the lifetime risk of breast, ovarian, prostate, and pancreatic cancers.

## Computational Pipeline
1. **Data Acquisition:** Obtained the raw transcript sequence (`NM_007294.4`) from NCBI Datasets in FASTA format(`real_brca1.fasta`).
2. **Dataset Preprocessing (`clean_fasta.py`):**
    - Filtered the multi-transcript NCBI dataset to isolate and store only the single target transcript(`NM_007294.4`) to optimize file size and computational memory.
3. **Custom FASTA Parsing (`day5_fasta_parser.py`):**
    - Strips metadata header lines(`>`).
    - Concatenates multi-line sequence strings into a single normalized uppercase DNA string.
    - Computes total nucleotide sequence length, individual base counts(A, T, G, C), and overall GC-Content percentage using native Python dictionary operations.
4. **Data Visualisation (`day6_ncbi_visualization.py`):**
    - Utilizes `matplotlib` to render publication-ready bar charts depicting base frequency distributions exported to `plots/brca1_base_distribution.png`.

## Outputs & Key Results
- **Total mRNA Sequence Length:** 7,152 base pairs
- **Base Breakdown:** A: 2,375 | T:1,771 | G: 1,618 | C: 1,388
- ****Calculated GC-Content:** 42.03%
- **Visualisation:** Generated high-resolution bar chart exported to `plots/brca1_base_distribution.png`.

## Project Structure
```text
bme_genomics/
├── data/
│   └── real_brca1.fasta
├── exports/
│   └── filtered_targets.csv
├── plots/
│   └── brca1_base_distribution.png
├── bme_genes.csv
├── clean_fasta.py
├── day1_refresher.py
├── day2_pandas_filter.py
├── day3_matplotlib_intro.py
├── day4_real_data.py
├── day5_fasta_parser.py
├── day6_ncbi_visualization.py
├── real_genome_data.csv
└── README.md
```
## How to Run
1. Ensure Python 3.x and `matplotlib` are installed.
2. Execute the parser:
    ```bash
    python day5_fasta_parser.py
    ```
3. Generate the distribution chart:
    ```bash
    python day6_ncbi_visualisation.py
    ```