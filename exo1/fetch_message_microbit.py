from microbit import *
import radio

radio.on()

while True:

    for n in range(3,4):
        radio.config(channel=n, length=200)

        msg = radio.receive()
        if msg:
            print(msg)
        sleep(500)


