from machine import Pin
import time
 
adc = machine.ADC(Pin(27))
 
while True:
     print(adc.read_u16())
     time.sleep(1)