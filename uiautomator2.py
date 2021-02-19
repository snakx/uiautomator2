# snakx Team
#
# Draft 1

import asyncio
import aiofiles
import requests as r

from ppadb.client_async import ClientAsync as AdbClient

class uiautomator2():

    async def __init__(self, host='127.0.0.1', port=5037):
        self.client = AdbClient(host, port)
        self.devices = await self.client.devices()

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
        device = self.client.device(serial)
        return device

    # Remote connect
    async def _rconnect(self, host, port):
        self.client.remote_connect(host, port)
        device = self.client.device(host+':'+str(port))
        return device

    # Remote disconnect
    async def _rdisconnect(self, host, port):
        try:
            self.client.remote_disconnect(host, port)
            return True
        except:
            return False

    # Shell
    async def _shell(self, device, cmd):
        return device.shell(cmd)

    # Pull
    async def _pull(self, device, p1, p2):
        return device.pull(p1, p2)

    # Package install
    async def _install(self, device, pk):
        return device.install(pk)

    # Package uninstall
    async def _uninstall(self, device, pk):
        return device.uninstall(pk)

    # Package installed
    async def _pk(self, device, pk):
        return device.is_installed(pk)

    # Send request to android-uiautomator2-server via http request
    async def _reg(self, url, data):
        return r.post(url, data=data).text