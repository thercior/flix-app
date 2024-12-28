from datetime import datetime
# import pandas as pd
import streamlit as st
from actors.service import ActorService
from genres.service import GenreService
from movies.services import MovieService
# from st_aggrid import AgGrid, ExcelExportMode


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.subheader('🎬 Lista de filmes')
        # Transformando em um dataframe

        cols = st.columns(3)

        for index, movie in enumerate(movies):
            with cols[index % 3]:  # Distribui os filmes entre as colunas
                st.container()
                st.markdown(
                    f"""
                    <div style="
                        border: 1px solid #ddd;
                        border-radius: 8px;
                        padding: 10px;
                        margin: 10px 0;
                        text-align: center;
                        background-color: rgba(25, 12, 3, 0.5);
                        width: 450px;
                        overflow: hidden;
                        justify-content: center;
                        align-items: center;
                    ">
                        <img src="{movie.get('capa', '')}"
                            alt="Capa do Filme"
                            style="width: 70%; height: 350px; object-fit: cover; border-radius: 8px;">
                        <h4>{movie['titulo']}</h4>
                        <p><strong>Gênero:</strong> {movie['genero']['nome']}</p>
                        <p><strong>Lançamento:</strong> {movie['ano']}</p>
                        <p><strong>Avaliação:</strong> {movie['avaliacao']} estrelas</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                # st.image(
                #     movie.get('capa'),
                #     caption=movie['titulo'],
                #     use_column_width=True,
                # )
                # st.write(f"**🎭 Gênero:** {movie.get('genero', 'N/A')}")
                # st.write(f"**📅 Ano:** {movie.get('ano', 'N/A')}")
                # st.write(f"**📅 Avaliacão:** {movie.get('avaliacao', 'N/A')}")
                # st.write(f"**📝 Resumo:** {movie.get('resumo', 'N/A')[:100]}...")

                if st.button(label="🔍 Detalhes", key=f'details_{movie['id']}'):
                    st.query_params['page'] = 'movie_details'
                    st.query_params['movie_id'] = movie['id']
                    st.rerun()

        # movies_df = pd.json_normalize(movies)

        # movies_df = movies_df.drop(columns=['atores', 'genero.id'])

        # AgGrid(
        #     data=movies_df,
        #     reload_data=True,
        #     columns_auto_size_mode=True,
        #     enableSorting=True,
        #     enableFilter=True,
        #     enableColResize=True,
        #     excel_export_mode=ExcelExportMode.MANUAL,
        #     key='movies_grid'
        # )
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
    cover_image = st.file_uploader('Capa do filme', type=['png', 'jpg', 'jpeg'])

    if st.button('Cadastrar'):
        movie_data = {
            "titulo": title,
            "ano": release_date,
            "genero": genre_names[selected_genre_name],
            "atores": selected_actors_ids,
            "resumo": resume,
        }

        if cover_image:
            movie_data['capa'] = cover_image

        new_movie = movie_service.create_movie(**movie_data)
        # new_movie = movie_service.create_movie(
        #     title=title,
        #     release_date=release_date,
        #     genre=genre_names[selected_genre_name],
        #     actors=selected_actors_ids,
        #     resume=resume
        # )

        if new_movie:
            st.success(f'Filme "{title}" cadastrado com sucesso!')
            st.rerun()
        else:
            st.error(f'Erro ao tentar cadastrar o filme {title}. Verifique os campos')


def show_movie_details(movie_id):
    st.title('🎥 Detalhes do Filme')

    movie_service = MovieService()
    movie = movie_service.get_movie_by_id(movie_id)

    if movie:
        st.image(
            movie.get('capa', ''),
            width=400,
            use_column_width=True,
        )

        st.markdown(f'### 🎬 {movie['titulo']}')
        st.write(f"**📅 Ano de Lançamento:** {movie['ano']}")
        st.write(f"**🎭 Gênero:** {movie['genero']['nome']}")
        st.write(f"**📝 Resumo:** {movie['resumo']}")
        st.write(f"** Avaliação:** {movie['avaliacao']}")
        st.write("**🎭 Atores:")
        for actor in movie['atores']:
            st.write(f'- {actor['nome']}')
    else:
        st.error("Filme não encontrado")
