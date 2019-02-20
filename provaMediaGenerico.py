#!/usr/bin/python3

import pychromecast as c

chromecast = c.Chromecast('109.167.119.154')

chromecast.wait()

print(chromecast.host)
print(chromecast.device.manufacturer)
print(chromecast.device.friendly_name)
print(chromecast.status.display_name)

#mc = chromecast.media_controller
#mc.play_media('http://wdex27.fastcdn.stream/lnholxljh75ee35huwrkcmx5jr2dyvmjzno5jgub6sfy7lw5z4mhratxb3rq/v.mp4','video/mp4')

#mc.block_until_active()
#mc.play()

print(chromecast.status.display_name)

