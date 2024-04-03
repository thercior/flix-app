import pandas as pd
import streamlit as st
from movies.services import MovieService
from review.service import ReviewService
from st_aggrid import AgGrid, ExcelExportMode


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

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

    st.subheader('Cadastrar uma Nova Avaliação')
    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['titulo']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))

    stars = st.number_input(label='Estrelas', min_value=0, max_value=5, step=1)
    comment = st.text_area(label='Comentário')

    if st.button('Cadastrar'):
        # Verificar aqui o erro que faz com que o retorno da api seja 200 e não 201 que é o certo.
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],
            stars=stars,
            comment=comment
        )

        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar a avalição. Por favor, verifique os campos')
