import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set GPIO 17 as input for backlight toggle with pull-up
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set GPIO 16 as input for fan control with pull-up
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)  # Set GPIO 26 as output for backlight, start HIGH
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)  # Set GPIO 4 as output for fan control, start LOW (fan off)

def toggle_backlight(channel):
    current_state = GPIO.input(26)
    GPIO.output(26, not current_state)
    print("Backlight toggled!")

def toggle_fan(channel):
    current_state = GPIO.input(4)
    GPIO.output(4, not current_state)
    print("Fan toggled!")

# Add event detection for buttons
GPIO.add_event_detect(17, GPIO.FALLING, callback=toggle_backlight, bouncetime=300)  # Debounce time to prevent multiple triggers
GPIO.add_event_detect(16, GPIO.FALLING, callback=toggle_fan, bouncetime=300)

print("Press the button on GPIO 17 to toggle the backlight.")
print("Press the joystick select button on GPIO 16 to toggle the fan.")

try:
    while True:
        # Main loop just chills, letting the callbacks do the heavy lifting
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nCleaning up!")
    GPIO.cleanup()  # Clean up GPIO on normal exit
