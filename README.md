# 9110
There appear to be few guides on the internet that walk someone through setting up a Raspberry Pi Pico and using an l9110 module with a DC fan and pwm.

There are some that come close, but add additional components and some that have mostly text,  however here is a simple example of how to use just those components in a very simple fashion.

Lots of documentation exist inside the pwm_runner file.


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

| Breadboard         | 5V Power|
| --------           | --------- |
| GND on Breadboard | -/5V |
| PWR on Breadboard | +/5V |






