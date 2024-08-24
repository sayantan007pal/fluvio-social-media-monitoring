import fluvio
import requests

def produce_messages():
    producer = fluvio.Fluvio.connect().topic_producer("social-media")

    # Example of collecting data from Twitter (replace with real API calls)
    tweets = [
        {"id": 1, "text": "Brand is doing great! #awesome", "user": "user1"},
        {"id": 2, "text": "This product is terrible. #fail", "user": "user2"}
    ]

    for tweet in tweets:
        producer.send_record(str(tweet), str(tweet['id']))

if __name__ == "__main__":
    produce_messages()
