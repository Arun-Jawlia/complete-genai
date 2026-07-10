#pylint: disable = all
import streamlit as st
import pickle
import joblib
import nltk
import pandas as pd
import sklearn

st.title("Movie Recommendation System")

with open('movies.pickle', 'rb') as m:
    movies = pickle.load(m)

similarity = joblib.load('similarity.joblib')

movie_names = movies['title'].values

def recommend(name):
    movie_index = movies[movies['title'] == name].index[0]
    recommendations = similarity[movie_index]
    movie_list = sorted(enumerate(recommendations), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        
    return recommended_movies


movie_name =  st.selectbox('Enter the Movie Name', movie_names)

if st.button('Recommend'):
    r = recommend(movie_name)
    st.write("The recommended movies are: ")
    for i in r:
        st.write(i)