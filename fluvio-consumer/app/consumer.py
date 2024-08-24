import fluvio
import requests
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return "positive" if analysis.sentiment.polarity > 0 else "negative"

def consume_messages():
    consumer = fluvio.Fluvio.connect().topic_consumer("social-media")
    for record in consumer.stream():
        tweet = eval(record.value_string())
        sentiment = analyze_sentiment(tweet["text"])
        print(f"Tweet ID: {tweet['id']}, Sentiment: {sentiment}")

if __name__ == "__main__":
    consume_messages()
