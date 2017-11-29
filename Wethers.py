import requests

class Wethers:
    def __init__(self, uri):
        self.check_uri_type(uri)
        self.uri = uri
        self.update()

    def get_wether(self):
        return None

    def get_wether_with_update(self):
        return None

    def get_wether_data_from_api(self):
        return None

    def update(self):
        self.__wether_api_dict = requests.get(self.uri).json()

    def __eq__(self, other):
        return None

    def __str__(self):
        return None

    def check_uri_type(self, uri):
        if not isinstance(uri,str):
            raise TypeError('\"uri\"\'s type must be \"str\"')
