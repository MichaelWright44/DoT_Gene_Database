import pandas as pd
from functools import reduce
import os
import PySimpleGUI as sg

#def contig_bins():
#remember to take 'first_path' in as an arguement and not have it found in this function
#also need result passed to it as well from the shell script
def Taxonomy(result, first_dir, tax_dir, save_dir):
    
    taxonomy = pd.DataFrame()
    cols_list =  ['gene_callers_id', 'contig', 'bin', 'co-assembly']
    first = pd.read_csv(first_dir, usecols = cols_list)

    first.rename(columns  = {'co-assembly':'co_assembly'}, inplace = True)

    result = result.merge(first, on = ['gene_callers_id' , 'contig', 'co_assembly'], how = 'outer')

    cols_list =  ['bin_name', 'total_scgs', 'supporting_scgs', 't_domain', 't_phylum', 't_class', 't_order', 't_family', 't_genus', 't_species']
    
    for subdir, dirs, files in os.walk(tax_dir):
        for file in files:
            if file.endswith('.txt'):
                data = pd.read_csv(os.path.join(subdir,file),usecols = cols_list, sep="\t")
                data['co_assembly'] = data.shape[0]*[file.split('-')[0].upper()]
                data.rename(columns  = {'bin_name':'bin'}, inplace = True)
                taxonomy = pd.concat([taxonomy, data])

    result = result.merge(taxonomy, on = ['bin', 'co_assembly'], how = "outer")
    result.to_csv(os.path.join(save_dir,'Results_with_taxonomy.tsv'),sep = '\t', index = False)

    return(result)