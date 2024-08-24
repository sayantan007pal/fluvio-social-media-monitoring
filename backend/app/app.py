from flask import Flask, request, jsonify
from backend.app.sentiment_analysis import analyze_sentiment
from pymongo import MongoClient
import os

app = Flask(__name__)

# Load environment variables
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['social_monitoring']

@app.route('/analyze', methods=['POST'])
def analyze():
    content = request.json
    text = content['text']
    sentiment = analyze_sentiment(text)
    response = {
        'text': text,
        'sentiment': sentiment
    }
    return jsonify(response)

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = list(db.posts.find({}, {'_id': 0}))
    return jsonify(posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
