import requests


class ApiBase:
    __base_url = 'http://flixfilmes.thrsolutions.com.br/api/v1/'

    @classmethod
    def get_base_url(cls):
        return cls.__base_url


class Auth:

    def __init__(self):
        self.__base_url = ApiBase.get_base_url()
        self.__auth_url = f'{self.__base_url}authentication/token/'

    def get_token(self, username, password):
        auth_payload = {
            'username': username,
            'password': password
        }
        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )

        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'Erro ao autenticar. Status code: {auth_response.status_code}'}
