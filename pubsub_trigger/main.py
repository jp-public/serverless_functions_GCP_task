import os
import json
import base64
from google.cloud import pubsub_v1
# Add any imports that you may need, but make sure to update requirements.txt

publisher = pubsub_v1.PublisherClient()
PROJECT_ID = "hybrid-flame-326117"


def restaurant_orders_pubsub(event, context):
    topic_path = "no data in event"
    if 'data' in event:
        decoded = base64.b64decode(event['data']).decode('utf-8')
        json_parsed = json.loads(decoded)
        topic_path = "wrong order type"
        message_bytes = decoded.encode('utf-8')
        if json_parsed["type"] == "takeout":
            topic_path = publisher.topic_path(PROJECT_ID, "restaurant_takeout_orders")
            publisher.publish(topic_path, data=message_bytes)
        elif json_parsed["type"] == "eat-in":
            topic_path = publisher.topic_path(PROJECT_ID, "restaurant_eat-in_orders")
            publisher.publish(topic_path, data=message_bytes)

    return topic_path
