import os
import sys
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'sa.json'

def upload_file_from_local(bucket_name, content):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(content)

    blob.upload_from_filename(content)

    print(
        f"{content} uploaded to GCS."
    )

upload_file_from_local('test-bucket-23432', sys.argv[1])