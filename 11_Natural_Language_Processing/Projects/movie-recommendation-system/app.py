#pylint: disable = all
import streamlit as st
import pickle
import joblib
import pandas as pd
import request

st.title("Movie Recommendation System")

with open('movies.pickle', 'rb') as m:
    movies = pickle.load(m)

similarity = joblib.load('similarity.joblib')

movie_names = movies['title'].values


def fetch_poster(movie_id):
    response = request.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=547ba3d8346c7535cd337047b4d7301a&language=en'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(name):
    movie_index = movies[movies['title'] == name].index[0]
    recommendations = similarity[movie_index]
    movie_list = sorted(enumerate(recommendations), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch post
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_movies_poster


movie_name =  st.selectbox('Enter the Movie Name', movie_names)

if st.button('Recommend'):
    names, poster = recommend(movie_name)
    st.write("The recommended movies are: ")
    
    col1, col2, col3, col4, col5 = st.bet_columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])