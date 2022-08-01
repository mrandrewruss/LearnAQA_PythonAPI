import requests


class MyRequests():
    @staticmethod
    def post(url: str, data: dict=None, headers: dict=None, cookies: dict=None):
        return MyRequests._send(url, data, headers, cookies, 'POST')

    @staticmethod
    def get(url: str, data: dict=None, headers: dict=None, cookies: dict=None):
        return MyRequests._send(url, data, headers, cookies, 'GET')

    @staticmethod
    def put(url: str, data: dict=None, headers: dict=None, cookies: dict=None):
        return MyRequests._send(url, data, headers, cookies, 'PUT')

    @staticmethod
    def delete(url: str, data: dict=None, headers: dict=None, cookies: dict=None):
        return MyRequests._send(url, data, headers, cookies, 'DELETE')

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):

        url = f"https://playgroud.learnqa.ru/api"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method == 'GET':
            responce = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == 'POST':
            responce = requests.get(url, data=data, headers=headers, cookies=cookies)
        elif method == 'PUT':
            responce = requests.get(url, data=data, headers=headers, cookies=cookies)
        elif method == 'DELETE':
            responce = requests.get(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        return responce