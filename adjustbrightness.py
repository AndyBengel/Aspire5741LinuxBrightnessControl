from sys import argv
import os
import sys

if os.geteuid() != 0:
    sys.exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

script, adjust_type = argv

tmp_max_brightness = open("/sys/class/backlight/intel_backlight/max_brightness")
tmp_current_brightness = open("/sys/class/backlight/intel_backlight/brightness")

new_brightness = 0
max_brightness = int(tmp_max_brightness.read())
min_brightness = 100
current_brightness = int(tmp_current_brightness.read())
brightness_toggle_level = 219

def adjust_brightness(new_level):
	new_level = str(new_level)
	target = open("/sys/class/backlight/intel_backlight/brightness", 'w')
	target.truncate()
	target.write(new_level)
	target.close()

if adjust_type == "up":
	if (current_brightness + brightness_toggle_level) < max_brightness :
		new_brightness = current_brightness + brightness_toggle_level
	else:
		new_brightness = max_brightness
	adjust_brightness(new_brightness)
elif adjust_type == "down":
	if  (current_brightness - brightness_toggle_level) > min_brightness:
		new_brightness = current_brightness - brightness_toggle_level
	else:
		new_brightness = min_brightness
	adjust_brightness(new_brightness)
else:
	print "Usage: 'sudo python adjustbrightness.py up' to increase brightness"
	print "'sudo python adjustbrightness.py down' to decrease brightness"
	





