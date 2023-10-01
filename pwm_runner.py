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


from machine import Pin, PWM
import time

B1A = Pin(0, Pin.OUT)
B1B = Pin(1, Pin.OUT)

""" 3-5V DC Hobby Fan 
The normal full power operation of the DC hobby fan is clockwise  
when holding the fan with the black wire on the left

#Forward
B1A.value(0); B1B.value(1) 
#Stop
B1A.value(1); B1B.value(1) 
#Backward
B1A.value(1); B1B.value(0)
#Stop
B1A.value(0); B1B.value(0)  
"""

""" 12V DC Fan 
#Forward
B1A.value(0); B1B.value(1)

All other combos do not make any difference as it appears to only move in one direction.

Therefore, by default B1B must be used as the speed with PWM:

#Stoped
pwm_speed = PWM(B1B, freq=1000, duty_u16=0)

#Full on 
pwm_speed = PWM(B1B, freq=1000, duty_u16=65535)

With full 12V DC on the L9110, the pi/pico/everything is stable.
"""


"""  NO PWM UP TO  THIS POINT !!! 

Software: I use 1 pin as direction pin and the other pin as speed pin.
If the direction is low then the motor will get power when ever the speed pin is high
so the speed the motor will spin at will be the duty with of the speed pin i.e PWM_duty = desired_speed.

If the direction is high then motor will spin the other way and the motor will get power anytime the speed pin is
low so you have to invert the PWM duty i.e PWM_duty = 100 - desired_speed
"""

#Left most connection on the L9110
B1A.value(0)
#Immediate to the right of B1A
B1B.value(1); 
pwm_speed = PWM(B1B, freq=1000, duty_u16=0)

"""
#Stop 
pwm_speed.duty_u16(0)
pwm.deinit()
#Full on 
pwm_speed.duty_u16(65535)
"""

while True:
    
    for x in range(25000,65535,1000):
        print(f"== {x} ==")
        pwm_speed.duty_u16(x)
        time.sleep(1)
        
    for x in range(65535,25000,-1000):
        print(f"== {x} ==")
        pwm_speed.duty_u16(x)
        time.sleep(1)
    
        

