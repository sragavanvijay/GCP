from google.cloud import storage
import datalab.storage as gcs


#this Function write the DF to storage as CSV file
def write_to_storage(bucket_name, df_to_write, file_name_in_bucket):
    gcs.Bucket(bucket_name).item(file_name_in_bucket).write_to(df_to_write.to_csv(),'text/csv')


def write_to_BigQuery(df, tabble_name):

    df.to_gbq(tabble_name, 'audit-tie-out-tool', chunksize=None,if_exists='append',verbose=False)



# tis function is to upload a file to storage bucket
#def upload_blob(bucket_name, source_file_name, destination_blob_name):
#  storage_client = storage.Client()
#  bucket = storage_client.get_bucket(bucket_name)
#  blob = bucket.blob(destination_blob_name)
#  blob.upload_from_filename(source_file_name)
#  print('File {} uploaded to {}.'.format(source_file_name,destination_blob_name))




#from google.cloud import bigquery
#
#
#client = bigquery.Client(project='audit-tie-out-tool')
#
## Instantiates a client
#bigquery_client = bigquery.Client()
#
## The name for the new dataset
#dataset_id = 'new_audit_files2'
#
## Prepares a reference to the new dataset
#dataset_ref = bigquery_client.dataset(dataset_id)
#dataset = bigquery.Dataset(dataset_ref)
#
## Creates the new dataset
#dataset = bigquery_client.create_dataset(dataset)
#
#print('Dataset {} created.'.format(dataset.dataset_id))