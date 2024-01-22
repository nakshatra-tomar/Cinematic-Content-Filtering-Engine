import streamlit as st
import pickle
import pandas
import requests

def recom(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recom_movies = []
    recom_poster = []
    for i in movies_list:
        movie_id = i[0]

        recom_movies.append(movies.iloc[i[0]]['title'])

        recom_poster.append(poster(i[0]))
    return recom_movies, recom poster

def poster(movie_id):
    response = requests.get( https://api.themoviedb.org/3/movie/{}.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


st.title('Cinematic Content Filtering Engine')

#movies_list = pickle.load(open('movies.pkl','rb')) #gives error

movies_dict = pickle.load(open('movies_dictionary.pkl', 'rb'))
movies = pandas.DataFrame(movies_dict)

similarity = pickle.load(open('cosine_sim_df.pkl','rb'))

selected_movie = st.selectbox(
    'What movie would you like suggestions for?',
    movies['title'].values)

if st.button('Recommend me something similar'):
    recommendations,posters = recom(selected_movie)

    for i in recommendations:
        st.write(i)