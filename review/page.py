import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


reviews = [
    {
        'id': 1,
        'stars': 5
    },
    {
        'id': 2,
        'stars': 3
    },
    {
        'id': 3,
        'stars': 4
    },
]


def show_reviews():
    st.title('Lista de Avaliações dos filmes')

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid'
    )
