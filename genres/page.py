import pandas as pd
import streamlit as st
from genres.service import GenreService
from st_aggrid import AgGrid, ExcelExportMode


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.subheader('Lista Gêneros')
        genres_df = pd.json_normalize(genres)

        # Importa para dataframe personalizado do streamlit-aggrid
        AgGrid(
            data=genres_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key='genres_grid'
        )
    else:
        st.warning('Nenhum Gênero foi encontrado')

    st.subheader('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')

    if st.button('Cadastrar'):
        new_genre = genre_service.create_genre(name=name)

        if new_genre:
            st.success(f'Gênero "{name}" cadastrado com sucessos')
            st.rerun()
        else:
            st.error(f'Erro ao tentar cadastrar o gênero {new_genre}. Por favor, verifique os campos')
