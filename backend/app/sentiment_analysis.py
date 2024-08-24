from transformers import pipeline

# Load sentiment analysis model
classifier = pipeline('sentiment-analysis')

def analyze_sentiment(text):
    result = classifier(text)[0]
    sentiment = {
        'label': result['label'],
        'score': result['score']
    }
    return sentiment
