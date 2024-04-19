import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def spotify_client():
    client_id = '147e9c580a6b46f4aefe806cf1ba75ec'  #Change based on your Spotify Client ID
    client_secret = 'deb63a0305904d2a9834587ed1522dec' #Change based on your Spotify Secret ID
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp

def fetch_song_details(query):
    sp = spotify_client()
    results = sp.search(q='track:' + query, type='track', limit=10)
    tracks = []
    for item in results['tracks']['items']:
        track_info = {
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'album': item['album']['name'],
            'image_url': item['album']['images'][0]['url']  
        }
        tracks.append(track_info)
    return tracks
