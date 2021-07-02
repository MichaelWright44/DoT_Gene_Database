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
              [sg.Text('Data Input Folder'), sg.Input(), sg.FolderBrowse()],
              [sg.Text('Combined Data Output Folder'), sg.Input(), sg.FolderBrowse()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Folder Selection', layout)

    event, values = window.read()
    window.close()
    
    return(values[0], values[1])

def Concat(data_path = '', save_path = '', data = None):
    
    data_dir, save_dir = data_path, save_path
    database = {}
    file_name = ''
    result_final = pd.DataFrame()

    if data == None:

        for subdir, dirs, files in os.walk(data_dir):
            for file in files:
                if file.endswith('.tsv'):
                    file = pd.read_csv(os.path.join(subdir,file), sep="\t")
                    result_final = pd.concat([result_final, file])
        print('- done concatenating files -')

    else:
        for item in data.keys():
            result_final = pd.concat([result_final, data[item]])
        print('- done concatenating files -')

    col_list = ['t_phylum', 't_class', 't_order', 't_family', 't_genus', 't_species']
    for col in result_final[col_list]:
        result_final.rename( columns = {col: col + '_gene'}, inplace = True)

    result_final.to_csv(os.path.join(save_dir,'Gene_Results.tsv'),sep = '\t', index = False)
    print('- done saving file -')
    
    return(result_final)

def main():
    data_dir, save_dir = GUI()
    Concat(data_dir, save_dir)
    
if __name__ == "__main__":
    main()