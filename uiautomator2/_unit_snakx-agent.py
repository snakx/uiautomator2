import uiautomator2 as ui
import _bridge as b
import _init as init
import _pk as p
import logging
from time import sleep

_bridge = b.Bridge()
snakx_agent = ui.Client()

# Init
client = _bridge._client()
download = init._Service()

# Download instrumentation
download._apk_cache_i()

# Download apk
download._apk_cache_r()

# Download jar
download._jar_cache()

# Download vbs
download._vbs_cache()

# Download bat
download._bat_cache()

# Devices
_devices = []
for device in client:
    _devices.append(device.serial)
    logging.debug(device.serial)

# Connect first device
device = None
if len(_devices) >= 1:
    device = _bridge._connect(_devices[0])
else:
    pass

# Connect snakx-agent
if device:
    snakx_agent.connect()

    sleep(3)

    # Ping
    ip = _bridge._ip(device)
    result = snakx_agent.ping(ip)
    logging.debug(result)