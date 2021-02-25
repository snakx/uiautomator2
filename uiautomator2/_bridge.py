import asyncio
import aiofiles
import _init as i
import _main as m
import logging
from time import sleep

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
        result = asyncio.run(self.adb._shell(device, "ip route"))
        # 192.168.178.0/24 dev wlan0 proto kernel scope link src 192.168.178.77
        _sp = str(result).split(' ')[8]
        return _sp

    def _shell(self, device, cmd):
        result = asyncio.run(self.adb._shell(device, cmd))
        return result

    def _req(self, url, data):
        result = asyncio.run(self.adb._reg(url, data))
        return result