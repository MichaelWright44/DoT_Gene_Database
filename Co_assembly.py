import pandas as pd
from functools import reduce
import os
import PySimpleGUI as sg

def GUI():
    """
    GUI for Co-assembly folder locations and for saving file locations
    """
    sg.theme('DarkBlue13')
    layout = [
              [sg.Text('Co-Assembly Input Folder'), sg.Input(), sg.FolderBrowse()],
              [sg.Text('Merged Data Output Folder'), sg.Input(), sg.FolderBrowse()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Folder Selection', layout)

    event, values = window.read()
    window.close()
    
    return(values[0], values[1])

def cell_merge (heading, merge_key, database, merge_column):
    """
    Merging cells on given column, for the input co-assembly
    """
    heading = str(merge_key[0]).split('-')[0]
    section = list(database[item] for item in merge_key)
    
    if 'taxonNames' not in merge_key[0]:
        database[heading + '_result'] = reduce(lambda  left,right: pd.merge(left,right, on=[merge_column], how ='outer'), section)
        
    elif 'taxonNames' in merge_key[0]:
        database[heading + '_result'] = database[heading + '_result'].merge(section[0], on = [merge_column], how = 'outer')
        
#need to not call the GUI for each use case in the concat script
database = {}
file_name = ''
data_dir, save_dir = GUI()

for subdir, dirs, files in os.walk(data_dir):
    dirs[:] = [d for d in dirs if d not in 'coassembly-bins-taxonomy']
    for file in files:
        if file.endswith('.txt'):
            file_name = file.split('.')[0]
            database[file_name] = pd.read_csv(os.path.join(subdir,file), sep="\t")
print('- done loading data -')

#drop the 'source' columns from select data-sets
for key in database:
    if 'source' in database[key].columns and 'gene-calls' not in key:
        database[key].drop(columns = 'source',inplace = True)

heading = list(database.keys())[0].split('-')[0]

#merge required columns into a single dataframe to export to .tsv
merging = [key for key in database if 'GENE-DETECTION' not in key and 'GENE-COVERAGES' not in key and 'taxonNames' not in key]
cell_merge(heading, merging, database, 'gene_callers_id')

merging = [key for key in database if 'taxonNames' in key]
cell_merge(heading,merging, database, 'taxon_id')
print('- done formatting data frames -')

database[heading + '_result']['co_assembly'] = database[heading + '_result'].shape[0]*[heading]
database[heading + '_result'].to_csv(os.path.join(save_dir,heading + '_merged.tsv'),sep="\t", index = False)
print('- Saving: %s -' % (heading + '_merged.tsv'))