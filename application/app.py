import streamlit as st
import pickle
import pandas


def recom(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recom_movies = []
    for i in movies_list:
        recom_movies.append(movies.iloc[i[0]]['title'])
    return recom_movies

st.title('Cinematic Content Filtering Engine')

#movies_list = pickle.load(open('movies.pkl','rb')) #gives error

movies_dict = pickle.load(open('movies_dictionary.pkl', 'rb'))
movies = pandas.DataFrame(movies_dict)

similarity = pickle.load(open('cosine_sim_df.pkl','rb'))

selected_movie = st.selectbox(
    'What movie would you like suggestions for?',
    movies['title'].values)

if st.button('Recommend me something similar'):
    recommendations = recom(selected_movie)
    for i in recommendations:
        st.write(i)