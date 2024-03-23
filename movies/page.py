import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


movies = [
    {
        'id': 1,
        'nome': 'Titanic'
    },
    {
        'id': 2,
        'nome': 'Bad Boys'
    },
    {
        'id': 3,
        'nome': 'Velozes e Furiosos'
    },
]


def show_movies():
    st.title('Lista de filmes')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid'
    )
