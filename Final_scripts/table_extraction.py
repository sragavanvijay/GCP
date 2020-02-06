import pandas as pd
import numpy as np
import re
import os
from PyPDF2 import PdfFileReader ##PyPDF2 need to be istalled
import tabula ## Tabula-py need to be installed
from tabula import read_pdf


dir_path='/home/vsam/tmp/'
all_files=os.listdir(dir_path)
pdf_files=[f for f in all_files if f.endswith(".pdf")]



for a in pdf_files:
    read_path=dir_path + '/' + a
    pdf = PdfFileReader(open(read_path,'rb'))
    #total_pages=pdf.getNumPages()
    create_file_name=os.path.splitext(a)[0].replace(" ", "_") + "_tables" + ".txt"
    file=open(dir_path + "/" + create_file_name, "a+")
    for f in range (0, pdf.getNumPages()+1):
        extract1=tabula.read_pdf(read_path, pages=f, multiple_tables=True,encoding = 'iso-8859-1')
        for i in extract1:
                i.to_csv(file, index=False, sep='\t', encoding='iso-8859-1',line_terminator='\n', header=False)
                file.write('\n')
                file.write('#########################################################################')
        file.write('\n')
        f=f+1
    #print(extract)
    file.close()
