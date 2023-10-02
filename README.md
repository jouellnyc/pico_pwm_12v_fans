# L9110 
There appear to be few guides on the internet that walk someone through setting up a Raspberry Pi Pico and using an L9110 module with a 12V DC fan/motor and [pwm](https://docs.micropython.org/en/latest/library/machine.PWM.html).

There are some that come close, but add additional components and some that have mostly text, however here is a simple example of how to use just those components in a very simple fashion.
There are caveats/warning about using 12V with 3.3/5V microcontrollers in some forums, but you can follow this setup safely - make sure the current does not exceed the rating of the L9110. 

For *smaller* hobby motors this is typically not a problem, but beware of their polarities and if they only move forward in one direction. The stall current at full 12V power, may exceed the the limit of L9110 if you were to try if full blast and will destroy the L9110(smoke/etc). This is %100 true of the larger fan in this repo.


Lots of documentation/urls exist inside the pwm_runner file as well.

NOTE: I connected the pi to "MotorB" because it was simply easier/closer to me at the time.

## Components
- [L9110](https://www.amazon.com/HiLetgo-H-bridge-Stepper-Controller-Arduino/dp/B00M0F243E)
- Pi Pico
- [Small 12 V Fan](https://www.aliexpress.us/item/3256802262312152.html)
- [Larger 12 V Fan](https://www.amazon.com/gp/product/B0BXDGWS4J/)
- [Power Jack Adapter](https://www.amazon.com/gp/product/B07C61434H/)


## Fritzing Schematic
![BreadBoard](images/L9110_bb.png)

## Connections
| Pico              | L9110| 
| --------          | --------- |
| GPIO 0            | Motor B1A |
| GPIO 1            | Motor B1B |

| Pico              | Breadboard|
| --------          | --------- |
| GND               | GND/rail  |

| Breadboard         | L9110|
| --------           | --------- |
| GND/rail           | GND      |
| +/5V/rail          | VCC      |

| Breadboard         | 5V Power (Terminal Block)|
| --------           | --------- |
| GND | -/5V |
| PWR | +/5V |

## ```pwm_runner```
This will run a for loop using PWM at high and slow speeds.  

So yes, you can control a 2-pin DC fan with Pico Pi and PWM.


## Comments on squeeling sound at low pwm frequency. 

Best to play around for what suits your fan.  See these links:

[Forum](https://picaxeforum.co.uk/threads/is-a-small-high-pitched-noise-normal-when-using-pwmout.9077/)

[Reddit](https://www.reddit.com/r/Motors/comments/ojn64m/12v_pwm_fan_makes_high_pitch_noise_when_hooked_up/)


## Notes for the L298N:
There are so many writes up on the L298N, here's 2:

[MCLAB](https://microcontrollerslab.com/dc-motor-l298n-driver-raspberry-pi-pico-tutorial/)
[HACK.IO](https://www.hackster.io/Ramji_Patel/raspberry-pi-pico-and-l298n-motor-driver-62bfa0)

Remember: 
- Remove the 'ENA' jumper and put GPIO4/Phys Pin 6 attached to it.
- This is valid for full speed:

IN1.low(); IN2.high() 
speed = PWM(Pin(4), freq=450, duty_u16=65535)

if you are setting up like this:
IN1 = Pin(3, Pin.OUT)
IN2 = Pin(2, Pin.OUT)

- Recall the 12V Fans do NOT move 'backwards'


