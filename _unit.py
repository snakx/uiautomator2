import __bridge__ as b
import _init as i
import pk as p

import logging

_bridge = b.Bridge()

# Init
client = _bridge._client()

# Devices
_devices = []
for device in client:
    _devices.append(device.serial)
    logging.debug(device.serial)

# Connect
device = None
if len(_devices) >= 1:
    device = _bridge._connect(_devices[0])
else:
    pass

# Download pk
download = i._Service()
download._apk_cache()

# Push apk
if device:
    _bridge._push(device, './'+ p._apk(), '/data/local/tmp/'+ p._apk())

# Install apk
if device:
    _bridge._install(device, '/data/local/tmp/'+ p._apk())

# Test Uninstall apk
#if device:
#     _bridge._uninstall(device)

# IP
if device:
    _bridge._ip(device)