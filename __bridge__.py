import asyncio
import aiofiles
import _init as i
import _main as m

class Bridge():

    adb = None

    def __init__(self):
        self.adb = m._main()

    def _download_apk(self):
        _dl = i._Service()
        _dl._apk_cache()

    def _client(self):
        client = asyncio.run(self.adb._init())
        return client

    def _devices(self):
        devices = asyncio.run(self.adb._devices)
        return devices

    def _connect(self, serial):
        device = asyncio.run(self.adb._connect(serial))
        return device

    def _push(self, device, src, dest):
        return asyncio.run(self.adb._push(device, src, dest))

    def _install(self, device, pk):
        return asyncio.run(self.adb._install(device, pk))

    def _uninstall(self, device):
        return asyncio.run(self.adb._uninstall(device))

    def _ip(self, device):
        return asyncio.run(self.adb.ip(device))