import time
from machine import Pin,PWM
 
#RGB
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

# Colors that we are going to display
colors = {"fuschia": (255, 0, 255), "yellow": (255,255,0), "aqua": (0, 255, 255)
          , "orange": (230, 138 , 0), "white": (255, 255 , 255)}

def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

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
        for key, color in colors.items():
            # Turn off each RGB
            turn_off_rgb()
            
            print(f"Displaying Color:: {key}")
            red, green, blue = color
            
            pwms[RED].duty_u16(map_range(red, 0, 255, 0, 65535))
            pwms[GREEN].duty_u16(map_range(green, 0, 255, 0, 65535))
            pwms[BLUE].duty_u16(map_range(blue, 0, 255, 0, 65535))
            time.sleep(2)
        
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        deinit_pwm_pins()

