import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid, ExcelExportMode
from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.subheader('Lista de atores/atrizes')
        actors_df = pd.json_normalize(actors)

        AgGrid(
            data=actors_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFiltering=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key='atores_grid'
        )
    else:
        st.warning('Nenhum Ator/Atriz foi encontrado')

    st.subheader('Cadastrar novo(a) Ator/Atriz')
    name = st.text_input('Nome(a) do Ator/Atriz')
    birthday = st.date_input(
        label='Data de nascimento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    nationality_dropdown = [
        'BRA',
        'Estados Unidos',
        'EUA',
        'Brasil',
        'Inglaterra',
        'Argentina',
        'Alemanha',
        'Austrália',
        'Holanda',
    ]
    nationality = st.selectbox(label='Nacionalidade', options=nationality_dropdown)

    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        if new_actor:
            st.success(f'Ator/Atriz "{name}" cadastrado(a) com sucesso!')
            st.rerun()
        else:
            st.error('Erro ao acdastrar o Ator/Atriz. verifique os campos novamente')
