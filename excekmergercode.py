# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and sett
import pandas as pd
import glob

path = "C:/Users/sai.s.ganesh.vandru/OneDrive - Accenture/Ganesh/input"
file_list= glob.glob(path+"/*.xlsx")

excl_list=[]

for file in file_list:
    excl_list.append(pd.read_excel(file))

excl_merged= pd.DataFrame()

for excl_file in excl_list:
    excl_merged=excl_merged.append(excl_file,ignore_index=True)
outputpath="C:/Users/sai.s.ganesh.vandru/OneDrive - Accenture/Ganesh/output/final1excel.xlsx"
excl_merged.to_excel(outputpath, index=False)

