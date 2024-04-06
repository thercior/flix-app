import streamlit as st
import plotly.express as px
from movies.services import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatísticas de Filmes')

    col1, col2 = st.columns(2, gap="large")

    # Adicionando estilos as colunas
    col1.markdown(
        "<style>div[data-testid='stHorizontalBlock'] div[data-testid='stBlock'{flex-direction:column}</style>",
        unsafe_allow_html=True
    )
    col2.markdown(
        "<style>div[data-testid='stHorizontalBlock'] div[data-testid='stBlock'{flex-direction:column}</style>",
        unsafe_allow_html=True
    )

    with col1:
        if len(movie_stats['filmes_por_genero']) > 0:
            st.subheader('Filmes por gênero')
            fig = px.pie(
                movie_stats['filmes_por_genero'],
                values='count',
                names='genero__nome',
                title='Filmes por gênero',
                height=400,
            )
            fig.update_layout(
                legend=dict(
                    orientation="v",
                    yanchor="bottom",
                    y=0.5,
                    xanchor="left",
                    x=0,
                    font=dict(
                        size=10,
                    )
                )
            )
            st.plotly_chart(fig)

    with col2:
        st.subheader('Quantidade de Filmes por gênero:')
        for genre in movie_stats['filmes_por_genero']:
            st.write(f"{genre['genero__nome']}: {genre['count']}")

    st.subheader('Total de Filmes cadastrados:')
    st.write(movie_stats['total_filmes'])

    st.subheader('Quantidade de Filmes por gênero:')
    for genre in movie_stats['filmes_por_genero']:
        st.write(f"{genre['genero__nome']}: {genre['count']}")

    st.subheader('Total de avaliações cadastradas:')
    st.write(movie_stats['total_reviews'])

    st.subheader('Média geral de estrelas nas avaliações:')
    st.write(movie_stats['media_avaliacoes'])
