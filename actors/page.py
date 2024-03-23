import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


actors = [
    {
        'id': 1,
        'nome': 'Will Smith'
    },
    {
        'id': 2,
        'nome': 'Angelina Jolie'
    },
    {
        'id': 3,
        'nome': 'Wagner Moura'
    },
]


def show_actors():
    st.title('Lista de atores/atrizes')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='atores_grid'
    )

    st.subheader('Cadastrar novo(a) Ator/Atriz')
    nome = st.text_input('Nome(a) do Ator/Atriz')

    if st.button('Cadastrar'):
        st.success(f'Ator/Atriz "{nome}" cadastrado(a) com sucesso!')
