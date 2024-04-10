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

st.markdown("""
            <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap" rel="stylesheet">
<style>
body, html {
    font-family: "Vazirmatn"!important;
    direction: RTL;
}
p, div, input, label, h1, h2, h3, h4, h5, h6 {
    font-family: "Vazirmatn"!important;
    direction: RTL;
}
@media(max-width:768px){
    [data-testid="column"] img {
        margin:0 auto;
        width: calc(33.3333% - 1rem) !important;
    }
    [data-testid="column"] * {
        text-align:center;
    }
    [data-testid="column"] {
        text-align:center;
        background:#fff;
        box-shadow:0 0 8px #d9d9d9;
        padding:10px;
    }
}
 [data-testid="column"] a {
    color: #000 !important;
    text-decoration: none !important;
}
[data-testid="column"] * {
    text-align:center;
}
[data-testid="column"] {
    text-align:center;
    background:#fff;
    box-shadow:0 0 8px #d9d9d9;
    padding:10px;
}
h2 div[data-testid="StyledLinkIconContainer"] {
    left: 0;
}
            </style>
""", unsafe_allow_html=True)
st.header("فیلم مورد علاقه تو پیدا کن :)")

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
selectvalue = st.selectbox("فیلمی که دوست داری انتخاب کن", movies_titles)

def recommend(movie_title):
    """Generate movie recommendations."""
    try:
        index = movie_data[movie_data['title'] == movie_title].index[0]
    except IndexError:
        return [], []
    
    distances = sorted(list(enumerate(movie_similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movie = []
    recommend_poster = []
    recommend_id = []
    for i in distances[1:6]:  # top 5 recommendations
        movie_id = movie_data.iloc[i[0]].id
        recommend_movie.append(movie_data.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))
        recommend_id.append(movie_id)
    return recommend_movie, recommend_poster, recommend_id

if st.button("بزن تا بهت پیشنهاد بدم"):
    movie_names, movie_posters, movie_ids = recommend(selectvalue)
    if movie_names and movie_posters and movie_ids:
        cols = st.columns(5)
        for col, name, poster,movie_id in zip(cols, movie_names, movie_posters,movie_ids):
            with col:
                link = f"https://www.themoviedb.org/movie/{movie_id}"
                # Embedding the poster and name in a clickable link
                st.markdown(f"<a href='{link}' target='_blank'><img src='{poster}' style='width:100%'><br>{name}</a>", unsafe_allow_html=True)

