import pandas as pd
import os
from functools import reduce
import PySimpleGUI as sg

import DoT_coassembly
import DoT_concat
import DoT_taxonomy
"""
 Step 1: Merge > Concat > Taxonamy
 
 required for this to work:
     - feed in each path for the location of the required files to their associated scripts
     - ensure that we don't ask main() for a return value and instead write another function to be called that returns the data and doesn't call the GUI
     - pass the merged and concated and binned data back to this script to then save the data in a resulting .tsv
     
"""

database = {}
data_dir  = input("folder path with co-assembly folders, taxonoamy folder and first.csv file: ")
tax_dir = ''

for subdir, dirs, files in os.walk(data_dir):
	if subdir.endswith("genes"):
		database[subdir.split('-')[0]] = DoT_coassembly.Merge(subdir, data_dir)
	elif subdir.endswith("taxonomy"):
		tax_dir = subdir

for subdir, dirs, files in os.walk (data_dir):
	for file in files:
		if file == 'first.csv':
			first_dir = os.path.join(data_dir,'first.csv')

result = DoT_concat.Concat(data_dir, data_dir,database)

DoT_taxonomy.Taxonomy(result, first_dir, tax_dir, data_dir)
