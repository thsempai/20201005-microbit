from microbit import *
import radio

radio.on()
radio.config(channel=1)

while True:
    radio.send("Hello people")
    sleep(1000)
