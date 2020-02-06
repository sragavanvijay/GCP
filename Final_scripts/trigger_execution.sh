#install all the necessary packages
bash install_packages.sh

#copies the pdf and excel sheets from starage bucket to compute engine.
bash copy_from_bucket.sh

#clean all the file names
python clean_file_names.py

#ectract all the text from the pdf file and save it as .txt file.
bash pdf_to_text.sh

#extract all the sheets of the given excel and save it as .txt
python excel_extract.py

#extract only the tables from the pddf file and save it as text.
python table_extraction.py
