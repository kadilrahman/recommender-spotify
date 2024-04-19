import pandas as pd
import nltk
import pickle
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import scipy.sparse as sp

# Download necessary NLTK resources
nltk.download('punkt')

data = pd.read_csv("spotify_millsongdata.csv")
data =data.sample(10000).drop('link', axis=1).reset_index(drop=True)

data['text'] = data['text'].str.lower().replace(r'^\w\s', ' ').replace(r'\n', ' ', regex = True)

import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenization(txt):
    tokens = nltk.word_tokenize(txt)
    stemming = [stemmer.stem(w) for w in tokens]
    return " ".join(stemming)

    data['text'] = data['text'].apply(lambda x: tokenization(x))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidvector = TfidfVectorizer(analyzer='word',stop_words='english')
matrix = tfidvector.fit_transform(data['text'])
similarity = cosine_similarity(matrix)

def recommendation(song_df):
    idx = data[data['song'] == song_df].index[0]
    distances = sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])
    
    songs = []
    for m_id in distances[1:21]:
        songs.append(data.iloc[m_id[0]].song)
        
    return songs

import pickle
pickle.dump(similarity,open('similarity.pkl','wb'))
pickle.dump(data,open('df.pkl','wb'))
