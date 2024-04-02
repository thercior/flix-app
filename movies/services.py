import streamlit as st
from movies.repository import MovieRepository


class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.movie_repository.get_movies()
        st.session_state.movies = movies
        return movies

    def create_movie(self, title, release_date, genre, actors, resume):
        movie = dict(
            titulo=title,
            genero=genre,
            ano=release_date,
            atores=actors,
            resumo=resume
        )
        new_movie = self.movie_repository.create_movie(movie)
        st.session_state.movies.append(new_movie)
        return new_movie

    def get_movie_stats(self):
        return self.movie_repository.get_movie_stats()
