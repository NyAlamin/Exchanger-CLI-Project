import json


class Storage:

    def __init__(self, filename):

        self.filename = filename

    def load(self):

        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return data

        except:
            return []

    def save(self, data):

        with open(self.filename, "w") as f:
            json.dump(data, f)