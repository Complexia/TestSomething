from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255) 
yellow = (255,255,0)

sense.show_letter("B",red)
sleep(1)
sense.show_letter("J",blue)
sleep(1)
sense.show_letter("O",green)
sleep(1)
sense.show_letter("R",white)
sleep(1)
sense.show_letter("N",yellow)
sleep(1)


sense.clear()