import requests

class Wethers:
    def __init__(self, uri):
        self.check_uri_type(uri)
        self.uri = uri
        self.update()

    def get_wether(self):
        return self.get_wether_data_from_api()

    def get_wether_with_update(self):
        self.update()
        return self.get_wether_data_from_api()

    def get_wether_data_from_api(self):
        rt = {}
        rt['location'] = self.__wether_api_dict['location']['city']
        rt['today'] = list(filter(lambda n: n['dateLabel'] == '今日', self.__wether_api_dict['forecasts']))[0]['telop']
        #rt['todayMaxTmp'] = list(filter(lambda n: n['dateLabel'] == '今日', self.__wether_api_dict['forecasts']))[0]['temperature']['max']['celsius']
        #rt['todayMinTmp'] = list(filter(lambda n: n['dateLabel'] == '今日', self.__wether_api_dict['forecasts']))[0]['temperature']['min']['celsius']
        rt['tomorrow'] = list(filter(lambda n: n['dateLabel'] == '明日', self.__wether_api_dict['forecasts']))[0]['telop']
        rt['tomorrowMaxTmp'] = list(filter(lambda n: n['dateLabel'] == '明日', self.__wether_api_dict['forecasts']))[0]['temperature']['max']['celsius']
        rt['tomorrowMinTmp'] = list(filter(lambda n: n['dateLabel'] == '明日', self.__wether_api_dict['forecasts']))[0]['temperature']['min']['celsius']
        return rt

    def update(self):
        self.__wether_api_dict = requests.get(self.uri).json()

    def __eq__(self, other):
        return None

    def __str__(self):
        return None

    def check_uri_type(self, uri):
        if not isinstance(uri,str):
            raise TypeError('\"uri\"\'s type must be \"str\"')
