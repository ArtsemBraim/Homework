class HistoryDict(dict):

    def __init__(self, val=None):
        super().__init__(val)
        self.history = []

    def __setitem__(self, key, value):
        if key in self.history:
            self.history.remove(key)

        if len(self.history) == 10:
            del self.history[0]

        self.history.append(key)

    def get_history(self):
        return self.history[::-1]


if __name__ == "__main__":
    d = HistoryDict({"foo": 42})
    d["bar"] = 5
    d["some"] = 10
    d["some2"] = 20
    d["some3"] = 30
    d["some4"] = 40
    d["some5"] = 50
    d["some6"] = 60
    d["some7"] = 70
    d["some8"] = 80
    d["some9"] = 90
    d["foo"] = 95
    d["some10"] = 100
    d["bar"] = 0
    print(d.get_history())
