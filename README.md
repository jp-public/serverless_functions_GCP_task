# Task on using serverless functions (GCP)

Aalto University CS-E4190 - Cloud Software and Systems

http_trigger: Simple function that triggers @POST with JSON content is made and saves content on cloud.

upload_trigger, vision: Triggers when an image file is uploaded to storage bucket. 
Detects text from image using Google Cloud Vision api and saves text to same bucket.

pubsub_trigger: Triggers when a msg is published to a Pub/Sub topic, publishes according to msg. 
