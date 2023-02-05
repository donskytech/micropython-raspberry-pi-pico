import time
from machine import Pin,PWM
 
# RGB
RED = 0
GREEN = 1
BLUE = 2

# Declare pins
pwm_pins = [13,14,15]
# Setup pins for PWM
pwms = [PWM(Pin(pwm_pins[RED])),PWM(Pin(pwm_pins[GREEN])),
                PWM(Pin(pwm_pins[BLUE]))]
# Set pwm frequency
[pwm.freq(1000) for pwm in pwms] 

def turn_off_rgb():
    pwms[RED].duty_u16(0)
    pwms[GREEN].duty_u16(0)
    pwms[BLUE].duty_u16(0)
    time.sleep(0.1)
    
# Deinitialize PWM on all pins
def deinit_pwm_pins():
    pwms[RED].deinit()
    pwms[GREEN].deinit()
    pwms[BLUE].deinit()

# main function
def main():
    while True:
        for pwm in pwms:
            # Turn off each RGB
            turn_off_rgb()
            
            for duty_value in range(0, 65535, 16):
                pwm.duty_u16(duty_value) 
                time.sleep(0.001)
            
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        deinit_pwm_pins()