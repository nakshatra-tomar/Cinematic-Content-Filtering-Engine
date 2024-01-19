import streamlit as st
import pickle
import pandas




st.title('Cinematic Content Filtering Engine')

#movies_list = pickle.load(open('movies.pkl','rb')) #gives error

movies_list = pickle.load(open('movies_dictionary.pkl', 'rb'))
movies = pandas.DataFrame(movies_list)


selected_movie = st.selectbox(
    'What movie would you like suggestions for?',
    movies['title'].values)

if st.button('Recommend me something similar'):
    st.write('aCC')

