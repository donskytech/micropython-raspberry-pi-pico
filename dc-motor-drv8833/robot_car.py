
from machine import Pin
from machine import PWM
import utime

'''
Class to represent our robot car
'''
class RobotCar:
    MAX_DUTY_CYCLE = 65535
    MIN_DUTY_CYCLE = 0
    def __init__(self, motor_pins, frequency=20000):
        self.left_motor_pin1 = PWM(Pin(motor_pins[0], mode=Pin.OUT))
        self.left_motor_pin2 = PWM(Pin(motor_pins[1], mode=Pin.OUT))
        self.right_motor_pin1 = PWM(Pin(motor_pins[2], mode=Pin.OUT))
        self.right_motor_pin2 = PWM(Pin(motor_pins[3], mode=Pin.OUT))
        # set PWM frequency
        self.left_motor_pin1.freq(frequency)
        self.left_motor_pin2.freq(frequency)
        self.right_motor_pin1.freq(frequency)
        self.right_motor_pin2.freq(frequency)
        
        self.current_speed = RobotCar.MAX_DUTY_CYCLE
        
    def move_forward(self):
        self.left_motor_pin1.duty_u16(self.current_speed)
        self.left_motor_pin2.duty_u16(RobotCar.MIN_DUTY_CYCLE)
        
        self.right_motor_pin1.duty_u16(self.current_speed)
        self.right_motor_pin2.duty_u16(RobotCar.MIN_DUTY_CYCLE)
           
    def move_backward(self):
        self.left_motor_pin1.duty_u16(RobotCar.MIN_DUTY_CYCLE)
        self.left_motor_pin2.duty_u16(self.current_speed)
        
        self.right_motor_pin1.duty_u16(RobotCar.MIN_DUTY_CYCLE)
        self.right_motor_pin2.duty_u16(self.current_speed)
        
    def stop(self):
        self.left_motor_pin1.duty_u16(RobotCar.MAX_DUTY_CYCLE)
        self.left_motor_pin2.duty_u16(RobotCar.MAX_DUTY_CYCLE)
        
        self.right_motor_pin1.duty_u16(RobotCar.MAX_DUTY_CYCLE)
        self.right_motor_pin2.duty_u16(RobotCar.MAX_DUTY_CYCLE)
        
    ''' Map duty cycle values from 0-100 to duty cycle 40000-65535 '''
    def __map_range(self, x, in_min, in_max, out_min, out_max):
      return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
        
    ''' new_speed is a value from 0% - 100% '''
    def change_speed(self, new_speed):
        new_duty_cycle = self.__map_range(new_speed, 0, 100, 40000, 65535)
        self.current_speed = new_duty_cycle

        
    def deinit(self):
        """deinit PWM Pins"""
        print("Deinitializing PWM Pins")
        self.stop()
        utime.sleep(0.1)
        self.left_motor_pin1.deinit()
        self.left_motor_pin2.deinit()
        self.right_motor_pin1.deinit()
        self.right_motor_pin2.deinit()
        
