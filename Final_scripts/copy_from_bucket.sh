#defining the bucket name.
bucket_name=audit_storage_bucket1

#Switching to /tmp directory

cd
cd tmp

#copy all the available .PDF, .xlsx, .xls files from landing directory(Bucket) to compute engine for extraction

gsutil cp gs://${Bucket_name}/tmp/*.pdf .
gsutil cp gs://${Bucket_name}/tmp/*.xlsx .
gsutil cp gs://${Bucket_name}/tmp/*.xls .


