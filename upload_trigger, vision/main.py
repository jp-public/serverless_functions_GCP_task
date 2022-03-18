import os
import io  # To read from saved file
from google.cloud import storage, vision
# Add any imports that you may need, but make sure to update requirements.txt


def image_to_text_storage(data, context):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(data['bucket'])
    blob = bucket.get_blob(data['name'])

    filename = blob.name
    if filename.endswith(".txt"):
        return
    blob.download_to_filename('/tmp/'+filename)

    client = vision.ImageAnnotatorClient()
    with io.open('/tmp/'+filename, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    text = response.full_text_annotation.text
    blob = storage.Blob(filename.partition('.')[0]+".txt", bucket)
    blob.upload_from_string(text, content_type="text/plain")

    return
