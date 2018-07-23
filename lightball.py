from gpiozero import LED, Button, PWMLED
from time import sleep
from signal import pause

	# setup pins for LEDS and motor
motor = LED(11)
red = PWMLED(17)
green = PWMLED(3)
blue = PWMLED(4)
white = LED(2)

red.frequency = 100

# setup pins for buttons

a = Button(13)
b = Button(6)
c = Button(26)

# set all leds to off

motor.off()
red.value = 0
green.value = 0
blue.value = 0
white.off()

r = 0

def white_on():
	white.on()

def white_off():
	white.off()

def motor_on():
	motor.on()

def motor_off():
	motor.off()

def rgb_on():
	global r
	r = r + 1
        if r == 1:
    	        red.value = 1
                green.value = 0 
                blue.value = 0
        if r == 2:
                red.value = 0
                green.value = 1
                blue.value = 0
        if r == 3:
                red.value = 0
                green.value = 0
                blue.value = 1
        if r == 4:
		red.pulse(fade_in_time=4, fade_out_time=4)
                green.value = 0
                blue.value = 0
	if r == 5:
                red.value = 0
                green.pulse(fade_in_time=4, fade_out_time=4)
                blue.value = 0
	if r == 6:
                red.value = 0
                green.value = 0
                blue.pulse(fade_in_time=4, fade_out_time=4)
	if r == 7:
                red.pulse(fade_in_time=4, fade_out_time=4)
                sleep(0.25)
                green.pulse(fade_in_time=3, fade_out_time=3)
                sleep(0.25)
                blue.pulse(fade_in_time=2, fade_out_time=2)
	if r == 8:
		red.value = 0
		green.value = 0
		blue.value = 0
                r = 0

a.when_pressed = white_on
a.when_released = white_off

b.when_pressed = rgb_on

c.when_pressed = motor_on
c.when_released = motor_off


pause()

