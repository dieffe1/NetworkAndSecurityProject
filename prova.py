#!/usr/bin/python3

import pychromecast as c

cc = c.Chromecast("192.168.1.108")

cc.wait()
cc.volume_down()
cc.quit_app()
