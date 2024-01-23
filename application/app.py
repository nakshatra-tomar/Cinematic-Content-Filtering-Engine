import streamlit as st
import pickle
import pandas
import requests



def recom(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recom_movies = []
    recom_poster = []
    recom_over = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recom_movies.append(movies.iloc[i[0]]['title'])

        recom_poster.append(poster(movie_id))
        recom_over.append(overview(movie_id))
    return recom_movies, recom_poster, recom_over

def poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=627a9e020bf5b7690422ef0f3171f8ce".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def overview(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=627a9e020bf5b7690422ef0f3171f8ce".format(movie_id))
    data = response.json()
    return data['overview']


st.title('ScreenSift.io')
heading = st.empty()

heading.subheader('⬅️ Pick a movie for recommendations')

#movies_list = pickle.load(open('movies.pkl','rb')) #gives error

def update_heading():
    heading.subheader("Here are the top 6 recommendations")


st.sidebar.title('Cinematic Content Filtering Engine')
st.sidebar.text('(Using NLP🤓🧪)')
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")


movies_dict = pickle.load(open('movies_dictionary.pkl', 'rb'))
movies = pandas.DataFrame(movies_dict)

similarity = pickle.load(open('cosine_sim_df.pkl','rb'))

selected_movie = st.sidebar.selectbox(
    'What movie would you like suggestions for?',
    movies['title'].values)

if st.sidebar.button('Recommend me something similar'):
    recommendations, posters, overviews = recom(selected_movie)
    update_heading()

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [recommendations[0], recommendations[1], recommendations[2], recommendations[3], recommendations[4],
         recommendations[5]])

    with tab1:
        col1a, col1b = st.columns([2, 3])  # Divide tab 1 into columns

        with col1a:
            st.image(posters[0], width=250)

        with col1b:
            st.header(recommendations[0])
            st.markdown(overviews[0])

    with tab2:
        col2a, col2b = st.columns([2, 3])  # Divide tab 2 into columns

        with col2a:
            st.image(posters[1], width=250)

        with col2b:
            st.header(recommendations[1])
            st.markdown(overviews[1])

    with tab3:
        col3a, col3b = st.columns([2, 3])  # Divide tab 3 into columns

        with col3a:
            st.image(posters[2], width=250)

        with col3b:
            st.header(recommendations[2])
            st.markdown(overviews[2])

    with tab4:
        col4a, col4b = st.columns([2, 3])  # Divide tab 4 into columns

        with col4a:
            st.image(posters[3], width=250)

        with col4b:
            st.header(recommendations[3])
            st.markdown(overviews[3])

    with tab5:
        col5a, col5b = st.columns([2, 3])  # Divide tab 5 into columns

        with col5a:
            st.image(posters[4], width=250)

        with col5b:
            st.header(recommendations[4])
            st.markdown(overviews[4])

    with tab6:
        col6a, col6b = st.columns([2, 3])

        with col6a:
            st.image(posters[5], width=250)

        with col6b:
            st.header(recommendations[5])
            st.markdown(overviews[5])


for i in range(16):
    st.sidebar.text("")

st.sidebar.write('Repository [link](https://github.com/nakshatra-tomar/Cinematic-Content-Filtering-Engine)')