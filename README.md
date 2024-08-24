# Social Media Monitoring App

## Overview

The Social Media Monitoring App is a tool designed to monitor, analyze, and visualize sentiment from social media platforms in real-time. By leveraging APIs and Fluvio's streaming data platform, this app collects data, processes it, and provides insightful visualizations for social media trends and sentiment analysis.

## Features

- **Real-time Data Streaming**: Utilizes Fluvio for producing and consuming social media data in real time.
- **Sentiment Analysis**: Integrates with Hugging Face Transformers for sentiment analysis of the collected data.
- **Interactive Frontend**: Provides an interactive interface built with React.js to visualize sentiment trends and insights.

## Architecture

The app is composed of four main components:

1. **Fluvio Producer**: Streams data from social media APIs.
2. **Fluvio Consumer**: Consumes the data stream, performs sentiment analysis, and stores the results.
3. **Backend**: A Flask-based API server that interacts with the frontend and provides analyzed data.
4. **Frontend**: A React.js application for visualizing sentiment analysis and trends.

## Social Media APIs Used

The app uses the following social media APIs:

- **Twitter API**: For streaming tweets based on specific hashtags or keywords.
- **Facebook Graph API**: For fetching posts, comments, and reactions.
- **Reddit API**: For streaming posts and comments from various subreddits.
- **Instagram Basic Display API**: For fetching public photos and videos from Instagram accounts.

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed on your machine.
- Fluvio CLI installed and configured.
- Access tokens and API keys for Twitter, Facebook, Reddit, and Instagram.

### Running the Application

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/social-media-monitoring.git
    cd social-media-monitoring
    ```

2. **Create a `.env` file** in the root directory with the following content:
    ```plaintext
    TWITTER_API_KEY=your_twitter_api_key
    TWITTER_API_SECRET_KEY=your_twitter_api_secret_key
    FACEBOOK_ACCESS_TOKEN=your_facebook_access_token
    REDDIT_CLIENT_ID=your_reddit_client_id
    REDDIT_SECRET=your_reddit_secret
    INSTAGRAM_ACCESS_TOKEN=your_instagram_access_token
    ```

3. **Build and start the Docker containers**:
    ```bash
    docker-compose up --build
    ```

4. **Access the Frontend**:
    Open your browser and navigate to `http://localhost:3000`.

### Directory Structure

- **frontend/**: Contains the React.js frontend code.
- **backend/**: Contains the Flask API server code.
- **fluvio-producer/**: Contains the code for the Fluvio producer that streams data from social media APIs.
- **fluvio-consumer/**: Contains the code for the Fluvio consumer that performs sentiment analysis.

### Docker Configuration

The application uses Docker Compose to manage the services. The `docker-compose.yml` file defines the following services:

- **frontend**: React.js application for the user interface.
- **backend**: Flask-based API server.
- **fluvio-producer**: Streams social media data.
- **fluvio-consumer**: Consumes data and performs sentiment analysis.

### Troubleshooting

- **No Active Fluvio Profile Error**: Ensure that Fluvio is correctly configured and that a profile is active.
- **Sentiment Analysis Not Working**: Make sure you have either TensorFlow or PyTorch installed in the backend service.
- **API Rate Limits**: Ensure your API keys and tokens are correctly configured and consider upgrading your API plan if necessary.

### Future Improvements

- **Additional Social Media Platforms**: Integrate more platforms such as LinkedIn, TikTok, and YouTube.
- **Advanced Sentiment Analysis**: Implement more sophisticated NLP techniques for better sentiment accuracy.
- **User Authentication**: Secure the app with user authentication and access control.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

