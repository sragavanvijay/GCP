import pdftotext
import os

def extract_pdf_text(dir_path):
    all_files = os.listdir(dir_path)
    pdf_files = [f for f in all_files if f.endswith(".pdf")]
    for file in pdf_files:
        file_name=os.path.splitext(file)[0].replace(" ", "_") + '_txt_extract' + ".txt"
        file_and_path_to_write=str(dir_path) + '/' + file_name
        print(file_and_path_to_write)
        read_path=str(dir_path) + '/' + file
        #print(read_path)
        #print(file_name_to_write)
        #a=1
        with open(read_path, "rb") as f:
            pdf = pdftotext.PDF(f) ## read the source PDF file
            txt_file = open(file_and_path_to_write, "w") ## open a txt file to write the contents of PDF file.
            for page in pdf:
                txt_file.write(page)
            txt_file.close()
        abs_txt_file_path = file_and_path_to_write
    return abs_txt_file_path



    ## extracting by running pdftotext in shell
#import os
#
#def extract_pdf_text(dir_path):
#    all_files = os.listdir(dir_path)
#    pdf_files = [f for f in all_files if f.endswith(".pdf")]
#    cmd = 'pdftotext -layout'
#    for file in pdf_files:
#        read_path=str(cmd) + " " + str(dir_path) + file
#        os.system(read_path)
