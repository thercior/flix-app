import requests
import streamlit as st
from login.service import logout


class MovieRepository:

    def __init__(self):
        self.__base_url = 'http://3.90.0.66/api/v1/'
        self.__movies_url = f'{self.__base_url}filmes/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_movies(self):
        response = requests.get(self.__movies_url, headers=self.__headers)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            logout()
            return None

        raise Exception(f'Erro ao obter dados da Api. Status code: {response.status_code}')

    def get_movie_stats(self):
        response = requests.get(f'{self.__movies_url}statistics/', headers=self.__headers)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            logout()
            return None

        raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')