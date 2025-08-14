import board
import pwmio
import time

# Define the LED pin
led_pin = board.GP12
led_pwm = pwmio.PWMOut(led_pin, frequency=1000, duty_cycle=0)


while True:
    for i in range(100):
        led_pwm.duty_cycle = int((i / 100) ** 2 * 65535)	#smooth fading for leds
        time.sleep(0.1)

while True:
    for i in range(100):
        led_pwm.duty_cycle = int((percentage / 100) * 65535)	# more linear function
        time.sleep(0.01)
