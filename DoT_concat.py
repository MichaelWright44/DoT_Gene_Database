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
              [sg.Text('Merged Co-Assemlby Files'), sg.Input(), sg.FolderBrowse()],
              [sg.Text('Concatenated Data Output Folder'), sg.Input(), sg.FolderBrowse()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Folder Selection', layout)

    event, values = window.read()
    window.close()
    
    return(values[0], values[1])

data_dir, save_dir = GUI()
database = {}
file_name = ''
result_final = pd.DataFrame()

for subdir, dirs, files in os.walk(data_dir):
    for file in files:
        if file.endswith('.tsv'):
            file = pd.read_csv(os.path.join(subdir,file), sep="\t")
            result_final = pd.concat([result_final, file])
print('- done concatenating files -')

result_final.to_csv(os.path.join(save_dir,'Gene_Results.tsv'),sep = '\t', index = False)
print('- done saving file -')
