import pytest
import allure
from auth import auth


def pytest_addoption(parser):
    # задаем опцию для запуска "окружение"
    parser.addoption('--host', action='store', default="https://www.chitai-gorod.ru/",
                     help="Адрес стенда")


@pytest.fixture(scope="session")
def client(request, worker_id):
    client = {}
    host = request.config.getoption("host")
    client["host_ui"] = host
    client["host_api"] = host.replace("www", 'web-gate')
    client["token"] = None
    client["token"] = auth.auth(client)
    client["worker_id"] = worker_id
    allure.attach(name='client', body="worker_id = " + str(worker_id)
                                      + "\n\nToken = " + client["token"],
                  attachment_type=allure.attachment_type.TEXT)
    return client
