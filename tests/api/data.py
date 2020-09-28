import requests
from tests import api


class GetData:
    url = f"{api.HOST}:{api.PORT}/api/data/"

    def send(self):
        return requests.get(self.url)


class PostData:
    url = f"{api.HOST}:{api.PORT}/api/data/"

    def __init__(self, string):
        self.string = string

    def send(self):
        return requests.post(self.url, json={'string': self.string})
