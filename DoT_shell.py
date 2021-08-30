import pandas as pd
import os
from functools import reduce
#import PySimpleGUI as sg

import DoT_coassembly
import DoT_concat
import DoT_taxonomy
import DoT_bin_info

"""
 Outline: co_assembly > concat > bin_info > taxonamy
"""
def GUI():
    """
    - GUI for Co-assembly folder locations and for saving file locations
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

def File_check(data, bin_dir, tax_dir):
	if data == None:
		raise Exception("Missing co-assembly data in file structure")
	elif bin_dir == '':
		raise Exception("Missing 'anvio_bins_COG_summaries' folder ")
	elif tax_dir == '':
		raise Exception("Missing 'coassembly-bins-taxonomy' folder")
	else:
		pass

def main():
	database = {}
	#data_dir, save_dir = GUI()
	data_dir = input("Input Data Folder: ")
	save_dir = input("File Output Folder: ")
	tax_dir = ''
	bin_dir = ''

	for subdir, dirs, files in os.walk(data_dir):

		if subdir.endswith("genes"):
			database[subdir.split('-')[0]] = DoT_coassembly.Merge(subdir, save_dir)
		elif subdir.endswith("taxonomy"):
			tax_dir = subdir
		elif subdir.endswith("summaries"):
			bin_dir = subdir

	File_check(database, bin_dir, tax_dir)

	co_assemblys = DoT_concat.Concat(data_dir, save_dir,database)

	bin_info = DoT_bin_info.bin_taxonomy(bin_dir)

	DoT_taxonomy.Taxonomy(co_assemblys, bin_info, tax_dir, save_dir)

	print('- Finished File Generation -')

if __name__ == '__main__':
	main()