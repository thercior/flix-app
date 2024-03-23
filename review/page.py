import pandas as pd
import streamlit as st
from review.service import ReviewService
from st_aggrid import AgGrid, ExcelExportMode


def show_reviews():
    reviews_service = ReviewService()
    reviews = reviews_service.get_reviews()

    if reviews:
        st.subheader('Lista de Avaliações dos filmes')
        # Montagem do Dataframe
        reviews_df = pd.json_normalize(reviews)

        AgGrid(
            data=reviews_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key='reviews_grid'
        )
    else:
        st.warning('Nenhuma avaliação foi encontrada')
