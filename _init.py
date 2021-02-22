import requests
import _main
import pk
import os
import logging

class _Service():
    
    def _apk_cache(self):
        try:
            logging.debug("Download apk {}".format(pk._current()))
            url = 'https://github.com/snakx/android-uiautomator2-server/raw/main/app/debug/{}'.format(pk._current())
            r = requests.get(url, allow_redirects=True)
        except Exception as e:
            logging.error(e.__context__)
            return False
        try:
            open('android-uiautomator2-server 0.1.0 Draft 1-debug.apk', 'wb').write(r.content)
            logging.debug('Download apk successfully completed')
            return True
        except Exception as e:
            logging.error(e.__context__)
            return False