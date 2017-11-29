import requests

class  OnePleaceWether:
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
        self.insert_today_wether_to_dic(rt)
        rt['tomorrow'] = list(filter(lambda n: n['dateLabel'] == '明日', self.__wether_api_dict['forecasts']))[0]['telop']
        rt['tomorrowMaxTmp'] = list(filter(lambda n: n['dateLabel'] == '明日', self.__wether_api_dict['forecasts']))[0]['temperature']['max']['celsius']
        rt['tomorrowMinTmp'] = list(filter(lambda n: n['dateLabel'] == '明日', self.__wether_api_dict['forecasts']))[0]['temperature']['min']['celsius']
        return rt

    def insert_today_wether_to_dic(self, rt):
        today = list(filter(lambda n: n['dateLabel'] == '今日', self.__wether_api_dict['forecasts']))[0]
        rt['today'] = today['telop']
        if today['temperature']['max'] is None:
            rt['todayMaxTmp'] = ''
        else:
            rt['todayMaxTmp'] = today['temperature']['max']['celsius']

        if today['temperature']['min'] is None:
            rt['todayMinTmp'] = ''
        else:
            rt['todayMinTmp'] = today['temperature']['min']['celsius']

    def insert_tomorrow_wether_to_dic(self, rt):
        tomorrow = list(filter(lambda n: n['dateLabel'] == '明日', self.__wether_api_dict['forecasts']))[0]
        rt['tomorrow'] = tomorrow['telop']
        if tomorrow['temperature']['max'] is None:
            rt['tomorrowMaxTmp'] = ''
        else:
            rt['tomorrowMaxTmp'] = tomorrow['temperature']['max']['celsius']

        if tomorrow['temperature']['min'] is None:
            rt['tomorrowMinTmp'] = ''
        else:
            rt['tomorrowMinTmp'] = tomorrow['temperature']['min']['celsius']

    def update(self):
        self.__wether_api_dict = requests.get(self.uri).json()

    def __eq__(self, other):
        return None

    def __str__(self):
        return None

    def check_uri_type(self, uri):
        if not isinstance(uri,str):
            raise TypeError('\"uri\"\'s type must be \"str\"')
