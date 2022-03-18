import os
import tempfile    # To create temporary file before uploading to bucket
from google.cloud import storage
# Add any imports that you may need, but make sure to update requirements.txt
storage_client = storage.Client()
bucket_name = os.environ.get('BUCKET_ENV_VAR', 'Specified environment variable is not set.')
bucket = storage_client.bucket(bucket_name)

def create_text_file_http(request):
    request_json = request.get_json()
    filecontent = request_json['fileContent']
    filename = request_json['fileName']
    blob = bucket.blob(filename)
    blob.upload_from_string(filecontent)

    return ({"filename": filename}, 200)