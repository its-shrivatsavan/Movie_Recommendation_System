# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:10:47 2023

@author: Shrivatsavan S
"""

import streamlit as st
import pickle
import requests #used for the api

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values


st.header("Movie Recommender System")
select_value = st.selectbox("Select movies from dropdown list", movies_list)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id) 
    data = requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path


def recommend_movie(movie):
      index = movies[movies['title']==movie].index[0]
      similarity_score = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector: vector[1])
      recommended_movies = []
      recommended_poster = []
      
      for i in similarity_score[1:7]:
        movies_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movies_id))
      
      return recommended_movies, recommended_poster
    
    
if st.button("Show Recommend"):
    movie_recommended, movie_poster = recommend_movie(select_value)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_recommended[1])
        st.image(movie_poster[1])
    with col2:
        st.text(movie_recommended[2])
        st.image(movie_poster[2])
    with col3:
        st.text(movie_recommended[3])
        st.image(movie_poster[3])
    with col4:
        st.text(movie_recommended[4])
        st.image(movie_poster[4])
    with col5:
        st.text(movie_recommended[5])
        st.image(movie_poster[5])