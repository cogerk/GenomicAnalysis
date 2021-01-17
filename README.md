# GenomicAnalysis

This project improves reproducibility and speeds up analysis of 16s sequencing results from complex microbial communities in biofilms for the Winkler Lab at the University of Washington.  

`Pipeline.ipynb` is a Jupyter Notebook takes the user's raw sequencing results and a taxonomic table. This is accomplished using USEARCH for data manipulations and sequence binning and the Ribosome Data Project database for taxonomic assignment. The user should be aware of how sequencing data is processed prior to their data's publication, so this notebook provides a step-by-step walk through of how data is manipulated and processed to yield the final table.

`Data Analysis.ipynb` is a  Jupyter Notebook that takes the output from `Pipeline.ipynb` and uses pandas to data clean it for easy visualization with either R, matplotlib, or even excel.


`_split_demux_fastq.py` is a supporting script required for the analysis performed in `Pipeline.ipynb`

`rdp_16s_v16.udb` is the database file associated with the Ribosome Database Project:
    _Wang, Q, G. M. Garrity, J. M. Tiedje, and J. R. Cole. 2007. Naïve Bayesian Classifier for Rapid Assignment of rRNA Sequences into the New Bacterial Taxonomy. Appl Environ Microbiol. 73(16):5261-5267; doi: 10.1128/AEM.00062-07 [PMID: 17586664]_

Note that this pipeline was designed using sequencing results from MR DNA. It will need to be modified if the raw sequencing data format differs from the MR DNA standard deliverable.
