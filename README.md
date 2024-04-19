# Music Recommender System

This project is a music recommender system that utilizes the Spotify API to fetch song data and recommends songs based on user input. It's built with Flask, a lightweight WSGI web application framework in Python. The Music Recommender System is an advanced, interactive tool designed to personalize music discovery. Leveraging the Spotify API, this system analyzes user inputs and song lyrics to recommend songs that resonate with individual tastes and preferences. It integrates machine learning algorithms to enhance accuracy and user engagement, making music discovery a deeply personalized experience.

## Features

- Song search functionality through the Spotify API.
- Song recommendations based on machine learning algorithms.
- Responsive web interface for interaction.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have a `Python 3.x` installed.
- You have a Spotify Developer account and have obtained your `client_id` and `client_secret`.
- You have a `Flask` installed for web development.
- You have a `Numpy` `Pandas` `nltk` `scikit-learn` installed for performing machine learning.
- You have a `spotipy` installed for using Spotify API.



## Installation

To install the Music Recommender System, follow these steps:

1. Clone the repository:
   git clone https://github.com/yourusername/music-recommender-system.git
   cd music-recommender-system

2. Set up a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
   pip install -r requirements.txt

## Configuration
Before running the application, you need to configure your Spotify API credentials. Set the environment variables for SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET:
export SPOTIPY_CLIENT_ID='your_spotify_client_id'
export SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'

## Running the Application
To run the application, 
1. Run the machine learning code 'notebooks/machine.py',execute the following command in the root directory:
   `python notebooks.machine`
   This will generate the pickle file of cosine similarity of the recommender model which is trained on the spotify dataset. Make sure to save the geenrated pickled files in the data folder. 

3. To run the application, execute the following command in the root directory:
   `python -m app.main`
   Navigate to http://127.0.0.1:5000/ in your web browser to use the application.



   

