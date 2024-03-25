import pandas as pd
import streamlit as st
from movies.services import MovieService
from st_aggrid import AgGrid, ExcelExportMode


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.subheader('Lista de filmes')
        # Transformando em um dataframe
        movies_df = pd.json_normalize(movies)

        movies_df = movies_df.drop(columns=['atores', 'genero.id'])

        AgGrid(
            data=movies_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key='movies_grid'
        )
    else:
        st.warning('Nenhum filme foi encontrado')
