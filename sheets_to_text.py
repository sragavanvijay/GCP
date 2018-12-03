import io
import numpy as np
import xlrd
import os
import pandas as pd
pd.options.display.float_format = '{:.2f}'.format


def extract_text_from_sheet(dir_path):
    #dir_path = '/home/jovyan/Test_excel_files/'

    all_files=os.listdir(dir_path)
    excel_files=[f for f in all_files if f.endswith((".xlsx",".xls"))]

    for a in excel_files:      # ''''##iterating through each excel file in the dir'''
        path= str(dir_path) + str(a)     # '''##building the path to read the excel file'''
        print(path)
        xls=pd.ExcelFile(path)
        sheet_names=xls.sheet_names
        all_sheets = pd.read_excel(xls, sheetname=sheet_names, na_values='NA')
        keys=all_sheets.keys()
        os.mkdir(dir_path + '/' + (os.path.splitext(os.path.basename(path))[0]).replace(" ", "_"))  #'''## creating a folder in the name of the excel file, replacing the " " with "_" and removind the file extension'''
        created_path=dir_path + a.rsplit(".", 1)[0].replace(" ","_") + '/'
        for i in keys:
            file_to_write = created_path + i.replace(" ","_") + '.txt'         #  '''##creating the file path and file name to write.'''
            all_sheets.get(i).to_csv(file_to_write, index=False, sep='\t', encoding='utf-8',line_terminator='\n')

