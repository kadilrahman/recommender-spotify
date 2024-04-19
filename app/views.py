from flask import Blueprint, render_template, request, jsonify
from .models import recommend_songs
from .spotify_api import fetch_song_details

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/recommend', methods=['POST'])
def recommend():
    song_query = request.json['song']
    try:
        song_details = fetch_song_details(song_query)
        return jsonify(song_details)
    except Exception as e:
        print("Error occurred: ", e)
        return jsonify({"error": "Failed to fetch song details"}), 500
