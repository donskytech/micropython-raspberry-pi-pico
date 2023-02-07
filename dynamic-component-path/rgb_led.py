import time
from machine import Pin,PWM

#RGB
RED = 0
GREEN = 1
BLUE = 2

# Class that wil interface with our RGB Module
class RGBLEDModule:
    def __init__(self, pwm_pins):
        self.pwms = [PWM(Pin(pwm_pins[RED])),PWM(Pin(pwm_pins[GREEN])),
                PWM(Pin(pwm_pins[BLUE]))]
        self.init_pwms()
    
    # Initialize PWM Pins
    def init_pwms(self):
        for pwm in self.pwms:
            pwm.freq(1000)
    
    # Deinitialize PWM fins
    def deinit_pwms(self):
        self.turn_off_rgb()
        for pwm in self.pwms:
            pwm.deinit()
    
    # Map RGB values from 0-255 to duty cycle 0-65535
    def map_range(self, x, in_min, in_max, out_min, out_max):
      return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

    # Turn off RGB
    def turn_off_rgb(self):        
        self.pwms[RED].duty_u16(0)
        self.pwms[GREEN].duty_u16(0)
        self.pwms[BLUE].duty_u16(0)
        time.sleep(0.1)
    
    # Set RGB Color
    def set_rgb_color(self, color):
        red, green, blue = color
        
        self.turn_off_rgb()  
        
        self.pwms[RED].duty_u16(self.map_range(red, 0, 255, 0, 65535))
        self.pwms[GREEN].duty_u16(self.map_range(green, 0, 255, 0, 65535))
        self.pwms[BLUE].duty_u16(self.map_range(blue, 0, 255, 0, 65535))
