import pandas as pd
import os

def bin_taxonomy (data_dir):
    """
    - Reads in data from 'anvio_bins_COG_summaries' generates a DataFrame and returns it
    """
    
    cols_list =  ['gene_callers_id', 'contig']
    bin_info = pd.DataFrame()
    counter = 0

    for subdir, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.txt'):
                data = pd.read_csv(os.path.join(subdir,file),usecols = cols_list, sep="\t")
                data['co_assembly'] = data.shape[0]*[file.split('-')[0].upper()]
                data['bin'] = data.shape[0]*[file.split('-')[1]]
                bin_info = pd.concat([bin_info, data])
                print('- assembling {} of {} files -' .format(counter, len(files)), end = '\r')
                counter += 1
    print('\n - done assembling files -')

    return(bin_info)