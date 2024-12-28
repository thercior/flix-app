import streamlit as st
from streamlit_option_menu import option_menu
from actors.page import show_actors
from genres.page import show_genres
from home.page import show_home
from login.page import show_login
from movies.page import show_movies, show_movie_details
from review.page import show_reviews


def main():
    query_params = st.query_params

    if 'token' not in st.session_state:
        # Initialize a token for the session
        show_login()
    else:
        page = query_params.get('page')

        st.title('Flix App')

        with st.sidebar:
            menu_option = option_menu(
                menu_title="Menu",
                options=['Início', 'Gêneros', 'Atores', 'Filmes', 'Avaliações'],
                icons=['house', 'film', 'person', 'camera-reels', 'stars'],
                menu_icon='menu-button-wide',
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "rgba(0, 0, 0, 0.5)"},
                    "icon": {"color": "red", "font-size": "25px"},
                    "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "rgba(0, 0, 0, 0.5)"},
                    "nav-link-selected": {"background-color": "rgba(0, 0, 156, 0.5)"},
                }
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

        if page == 'movie)details' and 'movie_id' in query_params:
            show_movie_details(query_params.get('movie_id'))


if __name__ == '__main__':
    main()
