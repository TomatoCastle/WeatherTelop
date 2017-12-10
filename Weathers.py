import OnePleaceWether

class Weathers:
    def __init__(self):
        self.Weathers = []

    def __str__(self):
        rtn = ''
        for i in self.Weathers:
            rtn += str(i)
        return rtn

    def add_weather(self, uri):
        self.Weathers.append(OnePleaceWether.OnePleaceWether(uri))

    def all_get_weather(self):
        rtn = []
        for i in range(0,len(self.Weathers)):
            rtn.append(self.get_weather(i))
        return rtn

    def get_weather(self, i):
        return self.Weathers[i].get_wether()

    def __len__(self):
        return len(self.Weathers)

    def __getitem__(self, item):
        return self.Weathers[item].get_wether()

    def __eq__(self, other):
        if not isinstance(other, Weathers):
            return False
        return self.Weathers == other.Weathers

