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
        movie_id = movies.iloc[i[0]].movie_id

        recom_movies.append(movies.iloc[i[0]]['title'])

        recom_poster.append(poster(movie_id))
    return recom_movies, recom_poster

def poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=627a9e020bf5b7690422ef0f3171f8ce".format(movie_id))
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

    col1, col2, col3, col4, col5  = st.columns(5)

    with col1:
        st.text(recommendations[0])
        st.image(posters[0])

    with col2:
        st.text(recommendations[1])
        st.image(posters[1])

    with col3:
        st.text(recommendations[2])
        st.image(posters[2])

    with col4:
        st.text(recommendations[3])
        st.image(posters[3])

    with col5:
        st.text(recommendations[4])
        st.image(posters[4])