import requests
import allure
from utils.prepare import func_allure_req


class Api:
    client = {}

    def __init__(self, client):
        self.client = client

    def _headers(self):
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json"
        }
        if self.client["token"] is not None:
            headers["Authorization"] = self.client["token"]
        return headers

    def post(self, path, headers=None, **kwargs):
        """
        :param path: путь к api запроса + resource + метод
        :param headers: заголовки запроса, по умолчанию будут указаны дефолтные
        :param kwargs: опции метода post
        :return: объект response
        """
        if headers is None:
            headers = self._headers()
        with allure.step(f"POST {path}"):
            response = requests.post(url=self.client["host_api"] + path, headers=headers, **kwargs)
            func_allure_req(response)
            return response

    def get(self, path, headers=None, **kwargs):
        """
        :param path: путь к api запроса + resource + метод
        :param headers: заголовки запроса, по умолчанию будут указаны дефолтные
        :param kwargs: опции метода get
        :return: объект response
        """
        if headers is None:
            headers = self._headers()
        with allure.step(f"GET {path}"):
            response = requests.get(url=self.client["host_api"] + path, headers=headers, **kwargs)
            func_allure_req(response)
            return response

    def put(self, path, headers=None, **kwargs):
        """
        :param path: путь к api запроса + resource + метод
        :param headers: заголовки запроса, по умолчанию будут указаны дефолтные
        :param kwargs: опции метода put
        :return: объект response
        """
        if headers is None:
            headers = self._headers()
        with allure.step(f"PUT {path}"):
            response = requests.put(url=self.client["host_api"] + path, headers=headers, **kwargs)
            func_allure_req(response)
            return response

    def delete(self, path, headers=None, **kwargs):
        """
        :param path: путь к api запроса + resource + метод
        :param headers: заголовки запроса, по умолчанию будут указаны дефолтные
        :param kwargs: опции метода delete
        :return: объект response
        """
        if headers is None:
            headers = self._headers()
        with allure.step(f"DELETE {path}"):
            response = requests.delete(url=self.client["host_api"] + path, headers=headers, **kwargs)
            func_allure_req(response)
            return response
