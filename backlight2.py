import RPi.GPIO as GPIO
import time

# Clean up any previous GPIO configurations
GPIO.cleanup()

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)  # TFT backlight
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)    # Fan control
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button for backlight
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Joystick button for fan

# Define the callback functions
def toggle_backlight(channel):
    current_state = GPIO.input(26)
    GPIO.output(26, not current_state)
    print("Backlight toggled!")

def toggle_fan(channel):
    current_state = GPIO.input(4)
    GPIO.output(4, not current_state)
    print("Fan toggled!")

# Add event detection for buttons
GPIO.add_event_detect(17, GPIO.FALLING, callback=toggle_backlight, bouncetime=300)
GPIO.add_event_detect(16, GPIO.FALLING, callback=toggle_fan, bouncetime=300)

print("Ready to roll! Press the button on GPIO 17 to toggle the backlight.")
print("Press the joystick select button on GPIO 16 to toggle the fan.")

try:
    # Chill here and wait for button presses
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nGraceful exit. Cleaning up...")
    GPIO.cleanup()  # Clean up GPIO on script exit
