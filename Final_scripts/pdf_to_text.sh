#navigate to the root dir
cd

#navigate to the /tmp dir
cd tmp

#extract the text from all the availabe .pdf files in the dir

for s in 'ls *.pdf'; do pdftotext -layout $s; done

