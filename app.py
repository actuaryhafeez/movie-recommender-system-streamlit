import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    """Fetches the movie poster for a given movie ID"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=77d860a9adac9c12b80a03d9db079dbb&language=en-US"
    data = requests.get(url).json()
    poster_path = data["poster_path"]
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path


def recommend(movie, movies, similarity):
    """Returns recommended movies based on the input movie"""
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


def display_recommendations(recommended_movie_name, recommended_movie_poster):
    """Displays recommended movies and their posters"""
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_name[0])
        st.image(recommended_movie_poster[0])
    with col2:
        st.text(recommended_movie_name[1])
        st.image(recommended_movie_poster[1])
    with col3:
        st.text(recommended_movie_name[2])
        st.image(recommended_movie_poster[2])
    with col4:
        st.text(recommended_movie_name[3])
        st.image(recommended_movie_poster[3])
    with col5:
        st.text(recommended_movie_name[4])
        st.image(recommended_movie_poster[4])


# Load data
movies = pickle.load(open("model/movie_list.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))
movie_list = movies["title"].values

# Display app header and input selection box
st.header("Movie Recommender System")
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# Display recommendations on button click
if st.button("Recommend"):
    recommended_movie_name, recommended_movie_poster = recommend(selected_movie, movies, similarity)
    display_recommendations(recommended_movie_name, recommended_movie_poster)
