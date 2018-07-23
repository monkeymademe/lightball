from gpiozero import LED, Button, PWMLED
from time import sleep
from signal import pause

# setup pins for LEDS and motor
motor = LED(11)
red = PWMLED(17)
green = PWMLED(3)
blue = PWMLED(4)
white = LED(2)

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

# set value for rotating color options
r = 0

# functions
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
	# increase r by 1 to cycle through the settings for the colors
	r = r + 1

	# color options
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
		# turn off all LEDs
		red.value = 0
		green.value = 0
		blue.value = 0
                # reset r to 0 so that the cycle can repeate
		r = 0

# when button a is pressed/released
a.when_pressed = white_on
a.when_released = white_off

# when button b is pressed
b.when_pressed = rgb_on

# when button c is pressed/released
c.when_pressed = motor_on
c.when_released = motor_off

# pause ending script
pause()

