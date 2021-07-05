import pandas as pd
import os
from functools import reduce
import PySimpleGUI as sg

import DoT_coassembly
import DoT_concat
import DoT_taxonomy
import DoT_bin_info
"""
 Step 1: Merge > Concat > Taxonamy
 
 required for this to work:
     - feed in each path for the location of the required files to their associated scripts
     - ensure that we don't ask main() for a return value and instead write another function to be called that returns the data and doesn't call the GUI
     - pass the merged and concated and binned data back to this script to then save the data in a resulting .tsv
     
"""
def GUI():
    """
    GUI for Co-assembly folder locations and for saving file locations
    """
    sg.theme('DarkBlue13')
    layout = [
              [sg.Text('Input Data Folder'), sg.Input(), sg.FolderBrowse()],
              [sg.Text('File Output Folder'), sg.Input(), sg.FolderBrowse()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Folder Selection', layout)

    event, values = window.read()
    window.close()
    
    return(values[0], values[1])

def main():
	database = {}
	data_dir, save_dir = GUI()
	tax_dir = ''
	bin_dir = ''

	for subdir, dirs, files in os.walk(data_dir):
		if subdir.endswith("genes"):
			database[subdir.split('-')[0]] = DoT_coassembly.Merge(subdir, save_dir)
		elif subdir.endswith("taxonomy"):
			tax_dir = subdir
		elif subdir.endswith("summaries"):
			bin_dir = subdir

	result = DoT_concat.Concat(data_dir, save_dir,database)

	bin_info = DoT_bin_info.bin_taxonomy(bin_dir)

	DoT_taxonomy.Taxonomy(result, bin_info, tax_dir, save_dir)

	print('- Finished File Generation -')

if __name__ == '__main__':
	main()