import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    re_movie_names = []
    re_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        re_movie_posters.append(fetch_poster(movie_id))
        re_movie_names.append(movies.iloc[i[0]].title)

    return re_movie_names, re_movie_posters


st.header('Search Something To Watch!')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendations'):
    re_movie_names, re_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    with col1:
        st.text(re_movie_names[0])
        st.image(re_movie_posters[0])

    with col2:
        st.text(re_movie_names[1])
        st.image(re_movie_posters[1])

    with col3:
        st.text(re_movie_names[2])
        st.image(re_movie_posters[2])

    with col4:
        st.text(re_movie_names[3])
        st.image(re_movie_posters[3])

    with col5:
        st.text(re_movie_names[4])
        st.image(re_movie_posters[4])

    with col6:
        st.text(re_movie_names[5])
        st.image(re_movie_posters[5])

    with col7:
        st.text(re_movie_names[6])
        st.image(re_movie_posters[6])

    with col8:
        st.text(re_movie_names[7])
        st.image(re_movie_posters[7])

    with col9:
        st.text(re_movie_names[8])
        st.image(re_movie_posters[8])

    with col10:
        st.text(re_movie_names[9])
        st.image(re_movie_posters[9])

