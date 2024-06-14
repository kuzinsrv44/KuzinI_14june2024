from utils.api import Api


def auth(client):
    client_tmp = client.copy()
    client_tmp["host_api"] = client_tmp["host_ui"]
    api = Api(client_tmp)
    response = api.get(path="")
    cookies = response.cookies.get_dict()
    token = cookies["access-token"].replace("%20", " ")
    return token
