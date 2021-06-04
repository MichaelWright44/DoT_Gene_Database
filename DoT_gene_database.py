import pandas as pd
from functools import reduce
import os

def cell_merge (merge_key, database, merge_column):
    heading = str(merge_key[0]).split('-')[0]
    section = list(database[item] for item in merge_key)
    
    if 'taxonNames' not in merge_key[0]:
        database[heading + '_result'] = reduce(lambda  left,right: pd.merge(left,right, on=[merge_column], how ='outer'), section)
        
    elif 'taxonNames' in merge_key[0]:
        database[heading + '_result'] = database[heading + '_result'].merge(section[0], on = [merge_column], how = 'outer')
        
def main():
    
    #reading in all gene data into one dictionary
    root_dir = os.path.dirname(os.path.realpath('Gene_database.ipynb'))
    database = {}
    file_name = ''
    result_final = pd.DataFrame()

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
             if file.endswith('.txt'):
                file_name = file.split('.')[0]
                database[file_name] = pd.read_csv(os.path.join(subdir,file), sep="\t")
    print('- done loading data -')

    #drop the 'source' columns from select data-sets
    for key in database:
        if 'source' in database[key].columns and 'gene-calls' not in key:
            database[key].drop(columns = 'source',inplace = True)

    #merge all required columns at correct locations
    section_names = ['azcf', 'azcs', 'azof', 'azos', 'bb16']

    merging = [key for key in database if 'GENE-DETECTION' not in key and 'GENE-COVERAGES' not in key and 'taxonNames' not in key]
    for item in section_names:
        section_name = [name for name in merging if item in name]
        cell_merge(section_name, database, 'gene_callers_id')

    merging = [key for key in database if 'taxonNames' in key]
    for item in section_names:
        section_name = [name for name in merging if item in name]
        cell_merge(section_name, database, 'taxon_id')

    print('- done formatting data frames -')

    #generate co-assembly columns for each sub-section
    #save each section to its own .csv file
    for name in section_names:
        database[name + '_result']['co_assembly'] = database[name + '_result'].shape[0]*[name]
        database[name + '_result'].to_csv(os.path.join(root_dir,name + 'DeepSenseAll.csv'), index = False)
        result_final = pd.concat([result_final, database[name +'_result']])
        print('- Saving: %s -' % (name + 'DeepSenseAll.csv'))
        
    result_final.to_csv(os.path.join(root_dir,'ResultDeepSenseALL.csv'), index = False)
    print( '- done saving files -')
    
if __name__ == '__main__':
    main()