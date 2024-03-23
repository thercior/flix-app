import streamlit as st
from actors.page import show_actors
from genres.page import show_genres
from home.page import show_home
from login.page import show_login
from movies.page import show_movies
from review.page import show_reviews


def main():

    if 'token' not in st.session_state:
        # Initialize a token for the session
        show_login()
    else:
        st.title('Flix App')

        menu_option = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Início', 'Gêneros', 'Atores', 'Filmes', 'Avaliações']
        )

        match menu_option:
            case 'Início':
                show_home()

            case 'Gêneros':
                show_genres()

            case 'Atores':
                show_actors()

            case 'Filmes':
                show_movies()

            case 'Avaliações':
                show_reviews()


if __name__ == '__main__':
    main()
