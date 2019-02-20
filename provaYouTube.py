#!/usr/bin/python3

import pychromecast as c
from pychromecast.controllers.youtube import YouTubeController

chromecast = c.Chromecast('212.10.46.242')

chromecast.wait()

print(chromecast.device.friendly_name)
print(chromecast.status.display_name)

yt = YouTubeController()
chromecast.register_handler(yt)

yt.play_video("tD8GLL1jz94")
#yt.play_video("19ro0Giif34", "RDtpt56VsvbJg")
#yt.play_next("7Zx_xAC1sxA")

print(chromecast.status.display_name)

