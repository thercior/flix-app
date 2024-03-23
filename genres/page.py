import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


genres = [
    {
        'id': 1,
        'nome': 'Ação'
    },
    {
        'id': 2,
        'nome': 'Suspense'
    },
    {
        'id': 3,
        'nome': 'Drama'
    },
    {
        'id': 4,
        'nome': 'Aventura'
    },
    {
        'id': 5,
        'nome': 'Terror'
    }
]


def show_genres():
    st.write('Lista Gêneros')

    # Importa para dataframe personalizado do streamlit-aggrid
    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid'
    )

    st.title('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')

    if st.button('Cadastrar'):
        st.success(f'Gênero "{name}" cadastrado com sucessos')
