import pandas as pd
from functools import reduce
import os
import PySimpleGUI as sg


def Taxonomy(result, bin_info, tax_dir, save_dir):
    """
    - Takes in results from concatenated co-assembly DataFrame & bin_info to merge
    - Uses 'gene_caller_id, contig, and co_assembly' to merge the two DataFrames
    """

    
    taxonomy = pd.DataFrame()

    result = result.merge(bin_info, on = ['gene_callers_id' , 'contig', 'co_assembly'], how = 'outer')

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
    
    print('- done saving gene results with taxonomy information')

    return(result)