"""

l9110

Need latest mp for params and pwm:
https://github.com/orgs/micropython/discussions/12162

DS - https://www.makerfabs.com/desfile/files/datasheet-l9110.pdf

Best picture - https://www.makerfabs.com/l9110-dual-channel-h-bridge-motor-driver-module-12v-800ma.html

Careful with 12 V - https://forums.raspberrypi.com/viewtopic.php?t=292239
                  - https://www.electroschematics.com/l9110-motor-driver-primer

How to set it up and use it - https://forum.micropython.org/viewtopic.php?t=5736

Other logical reference https://www.bananarobotics.com/shop/How-to-use-the-HG7881-(L9110)-Dual-Channel-Motor-Driver-Module

"""

from machine import Pin
import time

""" The normal full power operation of the DC hobby fan is clockwise """ 
""" when holding the fan with the black wire on the left             """

#Forward
#>>> B1A.value(0); B1B.value(1) 

#Stop
#>>> B1A.value(1); B1B.value(1) 

#Backward
#>>> B1A.value(1); B1B.value(0)

#Stop
#>>> B1A.value(0); B1B.value(0)  

#Pysical Labels
B1A = Pin(0, Pin.OUT)
B1B = Pin(1, Pin.OUT)

"""  NO PWM UP TO  THIS POINT !!! """
#Logical Labels
#direction = B1A
#speed     = B1B

"""
Quoting "https://forum.micropython.org/viewtopic.php?t=5736":

Software: I use 1 pin as direction pin and the other pin as speed pin.
If the direction is low then the motor will get power when ever the speed pin is high
so the speed the motor will spin at will be the duty with of the speed pin i.e PWM_duty = desired_speed.

If the direction is high then motor will spin the other way and the motor will get power anytime the speed pin is
low so you have to invert the PWM duty i.e PWM_duty = 100 - desired_speed
"""

#Set direction to low
#direction.value(0)
B1B.value(0); B1A.value(0)
pwm_speed = machine.PWM(B1A, freq=1000, duty_u16=0)

"""
#Stop 
pwm_speed.duty_u16(0)
#Full on 
pwm_speed.duty_u16(65535)

pwm.deinit()
"""

while True:
    
    for x in range(25000,65535,500):
        print(f"== {x} ==")
        pwm_speed.duty_u16(x)
        time.sleep(1)
        
    for x in range(65535,25000,-2000):
        print(f"== {x} ==")
        pwm_speed.duty_u16(x)
        time.sleep(1)
