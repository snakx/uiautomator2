import json

class Builder():

    def payload(self, cmd, action, params):
        if params:
            # {'cmd': 'action', 'action': 'startApp', 'params': {'packageName': 'com.instagram.android', 'mode': 1}}
            data = {
                "cmd": "{}".format(cmd),
                "action": "{}".format(action),
                "params": params
                }
        else:
            data = {
                "cmd": "{}".format(cmd),
                "action": "{}".format(action),
                "params": {
                    
                    }
                }
        return json.dumps(data)