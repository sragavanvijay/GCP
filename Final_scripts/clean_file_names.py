import io
#import numpy as np
#import xlrd
import os

def clean_file_names(dir_path):
    all_files=os.listdir(dir_path)
    
    excel_files_xlsx=[f for f in all_files if f.endswith(".xlsx")] 
    excel_files_xls=[f for f in all_files if f.endswith(".xls")]
    pdf_files=[f for f in all_files if f.endswith(".pdf")]
    
    for file in excel_files_xlsx:
        a=os.path.splitext(os.path.basename(file))[0].replace(" ", "_").replace(".", "_")
        new_file=dir_path+ a+'.xlsx'
        old_file=dir_path+ file
        os.rename(old_file,new_file)
        
    
    for file in excel_files_xls:
        a=os.path.splitext(os.path.basename(file))[0].replace(" ", "_").replace(".", "_")
        new_file=dir_path+ a+'.xls'
        old_file=dir_path+ file
        os.rename(old_file,new_file)
    
    
    for file in pdf_files:
        a=os.path.splitext(os.path.basename(file))[0].replace(" ", "_").replace(".", "_")
        new_file=dir_path+ a+'.pdf'
        old_file=dir_path+ file
        os.rename(old_file,new_file)
    
    
    

    
clean_file_names('/home/vsam/tmp')
