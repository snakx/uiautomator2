# uiautomator2

🐍 Python uiautomator2 bridge via http request

# How it works

**uiautomator2** is a python wrapper for the UIAutomator2 service. It connects via **[x86 UIAutomator2 Server](https://github.com/snakx/x86-uiautomator2-server)** on your pc to any android device and performs actions using **http interface** directly on the device.

# Example
```python
# params = {'x': 1, 'y': 1}
def click(self, host, params):
    return self.executor(host, 'action', 'click', params)
```
