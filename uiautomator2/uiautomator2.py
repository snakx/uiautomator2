import _bridge as b
import logging
import _json0 as jsn
from _url import *
import _x86 as j
import subprocess
import time
import os

class Client():
    
    def __init__(self):
        self.port = 7771
        self._bridge = b.Bridge()

    # adb shell pm list instrumentation
    def connect(self):
        try:
            # ToDo Implement shell script -> Linux, Mac
            subprocess.call('cscript "{}/uiautomator2.vbs"'.format(os.getcwd()))
            # Wait for execution 
            time.sleep(10)
            return True
        except Exception as e:
            logging.error(e.__context__)
            return False

    def _ping(self, host):
        action = jsn.Data()
        data = action.simple('ping')
        url = dump_json('http', host, str(self.port))
        result = self._bridge._req(url, data)
        return result