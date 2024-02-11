import RPi.GPIO as GPIO
import time

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)  # TFT backlight
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)    # Fan control
GPIO.setup(17, GPIO.IN)  # Button for backlight, already has a physical pull-up
GPIO.setup(16, GPIO.IN)  # Joystick button for fan, already has a physical pull-up

# Define the callback functions
def toggle_backlight(channel):
    current_state = GPIO.input(26)
    GPIO.output(26, not current_state)
    print("Backlight toggled!")

def toggle_fan(channel):
    current_state = GPIO.input(4)
    GPIO.output(4, not current_state)
    print("Fan toggled!")

# Remove any previous event detections
GPIO.remove_event_detect(17)
GPIO.remove_event_detect(16)

# Add event detection for buttons
GPIO.add_event_detect(17, GPIO.FALLING, callback=toggle_backlight, bouncetime=300)
GPIO.add_event_detect(16, GPIO.FALLING, callback=toggle_fan, bouncetime=300)

print("Ready to rock! Press the button on GPIO 17 to toggle the backlight.")
print("Hit the joystick select button on GPIO 16 to kick the fan into gear.")

try:
    # Kick back and wait for the show
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nPeace out! Cleaning up...")
    GPIO.cleanup()  # Clean up GPIO on script exit
