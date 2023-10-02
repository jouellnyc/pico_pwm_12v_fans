"""
Notes for the L298N:

https://microcontrollerslab.com/dc-motor-l298n-driver-raspberry-pi-pico-tutorial/
https://www.hackster.io/Ramji_Patel/raspberry-pi-pico-and-l298n-motor-driver-62bfa0

Remove the ENA jumper and put GPIO4/Phys Pin 6 attached to it.

Keeping in mind this is valid:

IN1.low(); IN2.high() 
speed = PWM(Pin(4), freq=450, duty_u16=65535)

For full speed using:
IN1 = Pin(3, Pin.OUT)
IN2 = Pin(2, Pin.OUT)

Recall the 12 V fans do NOT move 'backwards'

"""


from machine import Pin, PWM
from time import sleep

IN1 = Pin(3, Pin.OUT)
IN2 = Pin(2, Pin.OUT)

IN1.low(); IN2.high() 
speed = PWM(Pin(4), freq=450, duty_u16=0)

print("Starting Now")
      
while True:
        

        print("4")
        speed.duty_u16(40000)
        sleep(5)
        
        print("5")
        speed.duty_u16(50000)
        sleep(5)
        
        print("6")
        speed.duty_u16(65535)
        sleep(5)
        

