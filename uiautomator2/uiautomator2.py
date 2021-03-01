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

    # params = {'packageName': 'com.instagram.android', 'mode': 1}
    def startApp(self, host, params):
        return self.executor(host, 'action', 'startApp', params)

    # params = {'x': 1, 'y': 1}
    def click(self, host, params):
        return self.executor(host, 'action', 'click', params)

    # params = {'xoffset': 1, 'yoffset': 1, 'speed': 1}
    def flick(self, host, params):
        return self.executor(host, 'action', 'flick', params)

    # params = {'direction': 'left', 'percent': 1, 'steps': 1}
    def pinch(self, host, params):
        return self.executor(host, 'action', 'pinch', params)

    def pressback(self, host):
        return self.executor(host, 'action', 'pressBack', None)

    # params = {'keycode': 1, 'metastate': 1, 'duration': 1}
    def longPressKeyCode(self, host, params):
        return self.executor(host, 'action', 'longPressKeyCode', params)

    # params = {'keycode': 1}
    def pressKeyCode(self, host, params):
        return self.executor(host, 'action', 'pressKeyCode', params)

    # params = {'status': 'freeze'}
    def rotation(self, host, params):
        return self.executor(host, 'action', 'rotation', params)

    # Storage path: /data/local/tmp/screenshot.png
    def takeScreenshot(self, host):
        return self.executor(host, 'action', 'takeScreenshot', None)

    # params = {'direction': 'top', 'steps': 1}
    def scrollOrientation(self, host, params):
        return self.executor(host, 'action', 'scrollOrientation', params)

    # params = {'replace': 'true', 'text': ''}
    def scrollTo(self, host, params):
        return self.executor(host, 'action', 'scrollTo', params)

    # params = {'replace': 'true', 'text': ''}
    def setText(self, host, params):
        return self.executor(host, 'action', 'setText', params)

    # params = {'startX': 1, 'endX': 1, 'steps': 1}
    def swipe(self, host, params):
        return self.executor(host, 'action', 'swipe', params)

    # params = {'direction': '', 'steps': 1}
    def swipeOrientation(self, host, params):
        return self.executor(host, 'action', 'swipeOrientation', params)

    # params = {'flag': 'true'}
    def toast(self, host, params):
        return self.executor(host, 'action', 'toast', params)

    def touchDown(self, host):
        return self.executor(host, 'action', 'touchDown', None)

    def touchUp(self, host):
        return self.executor(host, 'action', 'touchUp', None)

    def touchMove(self, host):
        return self.executor(host, 'action', 'touchMove', None)

    # params = {'x': 1, 'y': 1, 'duration': 1}
    def touchLongClick(self, host, params):
        return self.executor(host, 'action', 'touchLongClick', params)

    # params = {'timeout': 1}
    def waitForIdle(self, host, params):
        return self.executor(host, 'action', 'waitForIdle', params)

    # params = {'x': 1, 'y': 1}
    def touchEvent(self, host, params):
        return self.executor(host, 'action', 'touchEvent', params)

    # params = {'strategy': '', 'selector': '', 'context': ''}
    def findElement(self, host, params):
        return self.executor(host, 'action', 'findElement', params)

    # params = {'multiple': 'false'}
    def find(self, host, params):
        return self.executor(host, 'action', 'find', params)

    # params = {'type': 'get'}
    def data(self, host, params):
        return self.executor(host, 'action', 'data', params)

    # params = {'attribute': ''}
    def getAttribute(self, host, params):
        return self.executor(host, 'action', 'getAttribute', params)

    def getDataDir(self, host):
        return self.executor(host, 'action', 'getDataDir', None)

    # params = {'dir': '', 'mode': 1, 'showtype': 1}
    def fileList(self, host, params):
        return self.executor(host, 'action', 'fileList', params)
    
    # params = {'compressLayout': 'true'}
    def compressedLayoutHierarchy(self, host, params):
        return self.executor(host, 'action', 'compressedLayoutHierarchy', params)

    def clearUiCache(self, host):
        return self.executor(host, 'action', 'clearUiCache', None)

    def clearCache(self, host):
        return self.executor(host, 'action', 'clearCache', None)

    def openRecentApps(self, host):
        return self.executor(host, 'action', 'openRecentApps', None)

    def getText(self, host):
        return self.executor(host, 'action', 'getText', None)

    def openNotification(self, host):
        return self.executor(host, 'action', 'openNotification', None)

    # params = {'package': ''}
    def jumpAppDetail(self, host, params):
        return self.executor(host, 'action', 'jumpAppDetail', params)

    # params = {'flag': 'true'}
    def getDeviceSize(self, host, params):
        return self.executor(host, 'action', 'getDeviceSize', params)

    def getParent(self, host):
        return self.executor(host, 'action', 'getParent', None)

    def getSize(self, host):
        return self.executor(host, 'action', 'getSize', None)

    def lock(self, host):
        return self.executor(host, 'action', 'lock', None)

    def rawSource(self, host):
        return self.executor(host, 'action', 'rawSource', None)

    def source(self, host):
        return self.executor(host, 'action', 'source', None)

    # params = {'action': ''}
    def startSettingAction(self, host, params):
        return self.executor(host, 'action', 'startSettingAction', params)

    # params = {'flag': 'add', 'name': '', 'text': '', 'packageName': ''}
    def uiWatcher(self, host, params):
        return self.executor(host, 'action', 'uiWatcher', params)

    def wakeup(self, host):
        return self.executor(host, 'action', 'wakeup', None)

    def stop(self, host):
        return self.executor(host, 'stop', '', None)