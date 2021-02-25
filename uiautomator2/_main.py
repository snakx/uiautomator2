import asyncio
import aiofiles
import requests as r
import logging
from subprocess import check_output
from time import sleep
from random import randint

from ppadb.client_async import ClientAsync as AdbClient

class _main():
        
    async def _init(self, host='127.0.0.1', port=5037):
        try:
            self.client = AdbClient(host, port)
            self.devices = await self.client.devices()
            return self.devices
        except Exception as e:
            logging.error(e.__context__)
            logging.error('snakx-agent has something wrong, auto recovering')
            check_output(["adb", "kill-server"])
            r = randint(5,10)
            logging.error('Sleeping {} s'.format(str(r)))
            sleep(r)
            check_output(["adb", "start-server"])
            await self._init()

    async def _devices(self):
        return self.devices

    async def _device(self, serial):
        devices = self.devices()

        for device in devices:
            if device.serial == serial:
                return device

        return None

    # Connect
    async def _connect(self, serial):
        try:
            device = await self.client.device(serial)
            return device
        except Exception as e:
            logging.error(e.__context__)
            return None

    # Push
    async def _push(self, device, src, dest):
        return await device.push(src, dest)

    # Pull
    async def _pull(self, device, src, dest):
        return await device.pull(src, dest)

    # Shell
    async def _shell(self, device, cmd):
        return await device.shell(cmd)

    # Package install
    async def _install(self, device, pk):
        return await device.install(pk)

    # Package uninstall
    async def _uninstall(self, device):
        return await device.uninstall()

    # Package installed
    async def _pk(self, device, pk):
        return await device.is_installed(pk)

    # Send request to android-uiautomator2-server via http request
    async def _reg(self, url, data):
        return r.post(url, data=data, timeout=60).text