# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and sett
import os
import pandas as pd
import glob

path = "C:/Users/sai.s.ganesh.vandru/OneDrive - Accenture/Ganesh/input"
file_list = glob.glob(path + "/*.xlsx")

excl_list = []
for file in file_list:
    # read each file and add filename as a column
    df = pd.read_excel(file)
    filename = os.path.basename(file)
    df['filename'] = filename
    excl_list.append(df)

excl_merged = pd.concat(excl_list, ignore_index=True)
outputpath = "C:/Users/sai.s.ganesh.vandru/OneDrive - Accenture/Ganesh/output/final6excel.xlsx"
excl_merged.to_excel(outputpath, index=False)
