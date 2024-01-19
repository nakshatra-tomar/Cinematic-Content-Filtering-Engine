import streamlit as st
import pickle
import pandas



st.title('Cinematic Content Filtering Engine')

movies_list = pickle.load(open('movies.pkl','rb'))

movies_list = movies_list['titles'].values

st.selectbox(
    'What movie would you like suggestions for?',
    ('Email', 'Home phone', 'Mobile phone'))

