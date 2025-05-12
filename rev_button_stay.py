"""

This Python script controls the speed of a 12V DC fan using Pulse Width Modulation (PWM). 
Due to the fan's reversed pin configuration (I noticed the GROUND lead controls the fan spinning not the VCC lead)
, where a high PWM duty cycle (typically meaning more "on" time) results in the fan being off or slower, 
and a low duty cycle (more "off" time in a standard setup) results 
in the fan being fully on or faster, the script implements the following:

Reversed PWM Logic: 
- The script treats 65535 as the maximum duty cycle (fan off) and 0 as the minimum duty cycle (full speed). 
  This is the core adaptation to the reversed pin behavior.

- Initialization for "Off": It starts by setting the PWM duty cycle to 65535, ensuring the fan begins in the off state, consistent with the reversed control.

- Speed Increase by Decreasing Duty: 
   Each time the connected button is pressed, the script decreases the PWM duty cycle. 
   This reduction in the duty cycle, because of the reversed pins, translates to the fan spinning faster. The speed increases by a fixed percentage of the remaining controllable range.

- Limiting to "Full Speed": 
  The script prevents the duty cycle from going below 0, which represents the maximum speed achievable with this reversed configuration.

- User Feedback: 
  It provides feedback on the initial state and each speed increase by printing the current duty cycle and the calculated speed percentage (taking into account the reversed logic).

- Safe Shutdown: 
  When the script is stopped, it sets the PWM duty cycle back to 65535, ensuring the fan is turned off as a clean exit.

In essence, the script inverts the typical PWM control behavior to correctly operate the 12V DC fan with its reversed pinout. 

So, by starting at the maximum duty cycle and decreasing it with each button press, the fan's speed progressively increases.

NOTE: 
- The small 2-pin adapter flips VCC to GROUND as well, introducing much confusion (so much for QA process on these components).
- This assumes you have a latching button connected to the pico...

"""
from machine import Pin, PWM
import time
from buttons import button, control_pin, other_pin

# PWM control constants
MAX_DUTY = 65535   # Maximum duty cycle (fan off)
MIN_DUTY = 0       # Minimum duty cycle (full speed)
START_DUTY = 52428 # Initial duty cycle (fan off)
DECREMENT = 0.2    # 20% increase in speed (decrease in duty) each button press

other_pin.value(1)
control_pin.value(1)

# Initialize PWM for speed control
pwm_speed = PWM(control_pin, freq=450, duty_u16=START_DUTY)

# Initial speed setting
current_duty = START_DUTY
pwm_speed.duty_u16(current_duty)

# Button state tracking
last_button_state = 1  # Assuming not pressed initially (pull-up)
debounce_time = 0.05   # Debounce time in seconds

print(f"Fan starting at PWM duty: {current_duty} ({((MAX_DUTY - current_duty) / MAX_DUTY) * 100:.1f}%)")

try:
    while True:
        # Read button state
        button_state = button.value()

        # Check for button press (transition from 1 to 0 with pull-up)
        if button_state == 0 and last_button_state == 1:
            # Button press detected - debounce
            time.sleep(debounce_time)
            if button.value() == 0:  # Confirm it's still pressed
                # Calculate new duty cycle (decrease by 20% of the remaining range)
                duty_range = MAX_DUTY - MIN_DUTY
                duty_decrement = int(duty_range * DECREMENT)
                new_duty = current_duty - duty_decrement

                # Cap at minimum value (full speed)
                if new_duty < MIN_DUTY:
                    new_duty = MIN_DUTY

                # Update speed if changed
                if new_duty != current_duty:
                    current_duty = new_duty
                    pwm_speed.duty_u16(current_duty)
                    print(f"Speed increased to: {current_duty} ({(1 - (current_duty / MAX_DUTY)) * 100:.1f}%)")
                else:
                    print("Maximum speed reached!")

        # Update last button state
        last_button_state = button_state

        # Small delay to reduce CPU usage
        time.sleep(0.01)

except KeyboardInterrupt:
    # Clean up - turn fan off
    pwm_speed.duty_u16(MAX_DUTY)
    print("Program stopped, fan turned off")



