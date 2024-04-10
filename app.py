import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    """Fetches movie poster from TMDB API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', "")
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path


# Load data
movie_data = pickle.load(open("movies.pkl", 'rb'))
movie_similarity = pickle.load(open("movie_similarity.pkl", 'rb'))

# Separate variables for DataFrame and titles
movies_titles = movie_data['title'].values


st.header("Movie Recommender System")

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
   
    ]


imageCarouselComponent(imageUrls=imageUrls, height=200)
selectvalue = st.selectbox("Select movie from dropdown", movies_titles)

def recommend(movie_title):
    """Generate movie recommendations."""
    try:
        index = movie_data[movie_data['title'] == movie_title].index[0]
    except IndexError:
        return [], []
    
    distances = sorted(list(enumerate(movie_similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movie = []
    recommend_poster = []
    for i in distances[1:6]:  # top 5 recommendations
        movie_id = movie_data.iloc[i[0]].id
        recommend_movie.append(movie_data.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))
    return recommend_movie, recommend_poster

if st.button("Show Recommend"):
    movie_names, movie_posters = recommend(selectvalue)
    if movie_names and movie_posters:
        cols = st.columns(5)
        for col, name, poster in zip(cols, movie_names, movie_posters):
            with col:
                st.text(name)
                st.image(poster)