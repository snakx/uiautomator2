import _bridge as b
import logging
import _json0 as jsn
from _url import *
import _x86 as j
from subprocess import check_output
import time
import os

class Client():
    
    def __init__(self):
        self._bridge = b.Bridge()

    def connect(self):
        try:
            # ToDo Implement shell script -> Linux, Mac
            logging.info("Stopping script host")
            out = check_output('taskkill /fi "imagename eq cscript.exe"')
            logging.debug(out)
            logging.info("Starting script host")
            out = check_output('cscript "{}/uiautomator2.vbs"'.format(os.getcwd()))
            logging.debug(out)
            # Wait for execution 
            time.sleep(10)
            return True
        except Exception as e:
            logging.error(e.__context__)
            return False

    def executor(self, host, cmd, action, params):
        builder = jsn.Builder()
        data = builder.payload(cmd, action, params)
        url = dump_route('http', host)
        logging.info(url)
        logging.info(data)
        result = self._bridge._req(url, data)
        return result

    def ping(self, host):
        return self.executor(host, 'action', 'ping', None)

    def startApp(self, host, params):
        return self.executor(host, 'action', 'startApp', params)