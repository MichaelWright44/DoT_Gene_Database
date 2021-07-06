
# DoT_Gene_Database
gene database for Dartmouth Ocean Tech primer references

## Installation

 - open command prompt or terminal and navigate to the folder this repo was cloned to
 - run the following:
```bash
pip install -r requirements.txt
```
## Usage 

 - before running any scripts in this repo, ensure that the gene data for processing is in the correct file structure as indicated below
 - +--- indidcates a sub folder
 - | indicates a file in that subfolder
 ```bash
[Data]                        #this is the folder that contains all of the following data

+---anvio_bins_COG_summaries  #contains all bin-contig-COG-summary files
|       AZCF-Bin_10-contigs-COG-summary.txt     
|       AZCF-Bin_100-contigs-COG-summary.txt
|       ...
|
+---azcf-ALL-genes            #this folder contains gene data for a specific co-assembly
|       azcf-COG-functions.txt
|       azcf-gene-calls.txt
|       azcf-genes-taxonNames.txt
|       azcf-genes-taxonomy.txt
|       azcf-KEGG-class-functions.txt
|       azcf-KEGG-module-functions.txt
|       azcf-KOfam-functions.txt
|       azcfGenes-GENE-COVERAGES.txt
|       azcfGenes-GENE-DETECTION.txt
|
+---[co-assembly]-All-genes   #same as the folder above, repeated for each co-assembly
|       ...
|
+---coassembly-bins-taxonomy  #contains taxonomy data for each co-assembly, in this example there are 5 co-assemblys
        azcf-scg-taxonomy-bins.txt
        azcs-scg-taxonomy-bins.txt
        azof-scg-taxonomy-bins.txt
        azos-scg-taxonomy-bins.txt
        bb16-scg-taxonomy-bins.txt
```

- After required files are stored as shown above, open command promt or terminal and navigate to the cloned repo folder
- run the following command:
```bash
python DoT_shell.py
```
- using the GUI that pops up, select the data directory that contains all the gene data for pre-processing
- now select a folder to store the output files. (this folder doesn't need to be in any particular format)

## Output files
- co-assembly_merged.tsv    | these files are the merged versions of your co-assembly folders
- Gene_Results.tsv          | this file is the gene info of all co-assemblys, but with no binning info

- Results_with_taxonomy.tsv | this file contains binning info, taxonomy, and gene data for all co-assemblys
 

