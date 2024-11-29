import json


class Dataset:

    def __init__(self, time, temperature):
        self.time = time
        self.temperature = temperature


    def __dict__(self):
        return {
            "time": self.time,
            "temperature": self.temperature
        }

    def __repr__(self):
        res = self.__dict__()
        return json.dumps(res, indent=2, default=str)