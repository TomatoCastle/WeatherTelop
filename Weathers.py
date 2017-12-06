import OnePleaceWether

class Weathers:
    def __init__(self):
        self.Weathers = []

    def __str__(self):
        return None

    def add_weather(self,uri):
        self.Weathers.append(OnePleaceWether.OnePleaceWether(uri))

    def all_get_weather(self):
        rtn = []
        for i in range(0,len(self.Weathers)):
            rtn.append(self.get_weather(i))
        return rtn

    def get_weather(self, i):
        return self.Weathers[i].get_wether()

    def __getitem__(self):
        return None

    def __eq__(self):
        return None