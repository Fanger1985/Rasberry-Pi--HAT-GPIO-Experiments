import RPi.GPIO as GPIO
import time

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)  # TFT backlight
GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)   # Fan control, start HIGH (fan on)

# Define the callback function for GPIO 16
def toggle_backlight(channel):
    current_state = GPIO.input(26)
    GPIO.output(26, not current_state)
    print("Backlight toggled!")

# Set up GPIO 16 for the backlight toggle button, with a physical pull-up
GPIO.setup(16, GPIO.IN)  

# Remove any previous event detections on GPIO 16 and add new detection
GPIO.remove_event_detect(16)
GPIO.add_event_detect(16, GPIO.FALLING, callback=toggle_backlight, bouncetime=300)

print("Press the joystick select button on GPIO 16 to toggle the backlight.")
print("Fan is running...")

try:
    # Just hang out and let the GPIO library handle the button press
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nShutting down, turning fan off...")
    GPIO.output(4, GPIO.LOW)  # Turn fan off
    GPIO.cleanup()  # Clean up GPIO on script exit
