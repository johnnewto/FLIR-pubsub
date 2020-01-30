#!/usr/bin/python

import sys
try:
    import mraa
except:
    pass
import time

# Use pin 7 by default
pin_no = 29

# Export the GPIO pin for use
pin = mraa.Gpio(pin_no)

# Small delay to allow udev rules to execute (necessary only on up)
time.sleep(0.1)

# Configure the pin direction
pin.dir(mraa.DIR_OUT)

# Loop
while True:
    # Turn the LED on and wait for 0.5 seconds
    pin.write(1)
    time.sleep(0.1)
    # Turn the LED off and wait for 0.5 seconds
    pin.write(0)
    time.sleep(0.1)