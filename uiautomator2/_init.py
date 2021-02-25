import requests
import _main
import _pk as p
import _x86 as j
import os
import logging

class _Service():
    
    # Instrumentation
    def _apk_cache_i(self):
        try:
            logging.debug("Download instrumentation apk {}".format(p._apk()))
            url = 'https://github.com/snakx/x86-uiautomator2-server/raw/main/bin/{}'.format(p._apk())
            logging.debug(url)
            r = requests.get(url, allow_redirects=True)
        except Exception as e:
            logging.error(e.__context__)
            return False
        try:
            open(p._apk(), 'wb').write(r.content)
            logging.debug('Download instrumentation apk successfully completed')
            return True
        except Exception as e:
            logging.error(e.__context__)
            return False

    # Release
    def _apk_cache_r(self):
        try:
            logging.debug("Download release apk {}".format(p._apk2()))
            url = 'https://github.com/snakx/x86-uiautomator2-server/raw/main/bin/{}'.format(p._apk2())
            logging.debug(url)
            r = requests.get(url, allow_redirects=True)
        except Exception as e:
            logging.error(e.__context__)
            return False
        try:
            open(p._apk2(), 'wb').write(r.content)
            logging.debug('Download release apk successfully completed')
            return True
        except Exception as e:
            logging.error(e.__context__)
            return False

    # Jar
    def _jar_cache(self):
        try:
            logging.debug("Download x86 jar {}".format(p._apk2()))
            url = 'https://github.com/snakx/x86-uiautomator2-server/raw/main/out/artifacts/x86_uiautomator2_server_jar/{}'.format(j._jar())
            logging.debug(url)
            r = requests.get(url, allow_redirects=True)
        except Exception as e:
            logging.error(e.__context__)
            return False
        try:
            open(j._jar(), 'wb').write(r.content)
            logging.debug('Download x86 jar successfully completed')
            return True
        except Exception as e:
            logging.error(e.__context__)
            return False

    # vbs
    def _vbs_cache(self):
        try:
            logging.debug("Download vbs script {}".format(p._apk2()))
            url = 'https://github.com/snakx/x86-uiautomator2-server/raw/main/bin/uiautomator2.vbs'
            logging.debug(url)
            r = requests.get(url, allow_redirects=True)
        except Exception as e:
            logging.error(e.__context__)
            return False
        try:
            open('uiautomator2.vbs', 'wb').write(r.content)
            logging.debug('Download vbs script successfully completed')
            return True
        except Exception as e:
            logging.error(e.__context__)
            return False

    # bat
    def _bat_cache(self):
        try:
            logging.debug("Download shell script {}".format(p._apk2()))
            url = 'https://github.com/snakx/x86-uiautomator2-server/raw/main/bin/uiautomator2.bat'
            logging.debug(url)
            r = requests.get(url, allow_redirects=True)
        except Exception as e:
            logging.error(e.__context__)
            return False
        try:
            open('uiautomator2.bat', 'wb').write(r.content)
            logging.debug('Download shell script successfully completed')
            return True
        except Exception as e:
            logging.error(e.__context__)
            return False