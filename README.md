# L9110 
There appear to be few guides on the internet that walk someone through setting up a Raspberry Pi Pico and using an L9110 module with a 12V DC fan/motor and pwm.

There are some that come close, but add additional components and some that have mostly text, however here is a simple example of how to use just those components in a very simple fashion.
There are caveats/warning about using 12V with 3.3/5V microcontrollers in some forums, but you can follow this setup safely - make sure the current does not exceed the rating of the L9110. For *smaller* hobby motors, this is typically not a problem, but beware of their polarities and if they only move forward in one direction. The stall current at full 12V power, may exceed the L9110 if you were to try if full blast and destroy the L9110(smoke/etc). This is %100 true of the larger fan in this repo.


Lots of documentation/urls exist inside the pwm_runner file as well.

NOTE: I connected the pi to "MotorB" because it was simply easier/closer to me at the time.

## Components
- [L9110](https://www.amazon.com/HiLetgo-H-bridge-Stepper-Controller-Arduino/dp/B00M0F243E)
- Pi Pico
- [Small 12 V Fan](https://www.aliexpress.us/item/3256802262312152.html)
- [Larger 12 V Fan](https://www.amazon.com/gp/product/B0BXDGWS4J/)
- [Power Jack Adapter](https://www.amazon.com/gp/product/B07C61434H/)


**Fritzing Schematic**
![BreadBoard](images/L9110_bb.png)

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

