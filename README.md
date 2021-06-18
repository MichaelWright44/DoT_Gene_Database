# DoT_Gene_Database
gene database for Dartmouth Ocean Tech primer references

- removed tracking for large input .txt files and output .csv files
- local file storage required until remote server can be setup


## Installation

 - open command prompt or terminal and navigate to the folder this repo was cloned to
 - run the following:
      pip freeze > requirements.txt

## Usage 
 - before running any scripts in this repo, ensure that your gene data for precessing is seperated by co-assembly (i.e azcf, azcs, bb16, ...)
 - run DoT_coassembly.py and select the first co-assembly folder you want to merge, and the location you want to save the result.tsv file to
 - you should now have a merged .tsv file of each co-assembly in 1 folder
 - run DoT_concat.py and select the input folder as the location of the merged files


 TODO: update with relevent steps for third script
