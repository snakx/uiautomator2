import json

class Data():

    def simple(self, action):
        data = {}
        data['action'] = action
        return json.dumps(data)