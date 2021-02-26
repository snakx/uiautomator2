import json

class Builder():

    def payload(self, cmd, action, params):
        if params:
            data = {
                "cmd": "{}".format(cmd),
                "action": "{}".format(action),
                "params": {
                    params
                    }
                }
        else:
            data = {
                "cmd": "{}".format(cmd),
                "action": "{}".format(action),
                "params": {
                    
                    }
                }

        return json.dumps(data)