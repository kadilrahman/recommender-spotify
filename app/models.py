import pickle
import os

def load_model():
    with open(os.path.join('..', 'data', 'similarity.pkl'), 'rb') as f:
        similarity = pickle.load(f)
    with open(os.path.join('..', 'data', 'df.pkl'), 'rb') as f:
        df = pickle.load(f)
    return similarity, df

def recommend_songs(song):
    similarity, df = load_model()
    song_index = df[df['song'].str.lower() == song.lower()].index[0]
    distances = sorted(list(enumerate(similarity[song_index])), key=lambda x: x[1], reverse=True)
    recommendations = [df.iloc[i[0]].song for i in distances[1:11]]
    return recommendations
