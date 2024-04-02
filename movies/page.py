from datetime import datetime
import pandas as pd
import streamlit as st
from actors.service import ActorService
from genres.service import GenreService
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

    st.subheader('Cadastrar novo filme')

    title = st.text_input('Título')
    release_date = st.date_input(
        label="Data de lançamento",
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format="DD/MM/YYYY"
    )

    # Coleta informações de gêneros
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['nome']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Gênero', list(genre_names.keys()))

    # Coleta atores/atrizes cadastrados
    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['nome']: actor['id'] for actor in actors}
    selected_actors_names = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_names]
    resume = st.text_area('Resumo')

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume
        )

        if new_movie:
            st.rerun()
        else:
            st.error(f'Erro ao tentar cadastraro filme {title}. Verifique os campos')
