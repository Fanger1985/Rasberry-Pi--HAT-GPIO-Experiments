import RPi.GPIO as GPIO
import time

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)  # TFT backlight
GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)   # Fan control, start HIGH (fan on)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button for backlight toggle with pull-up

# Function to toggle the backlight
def toggle_backlight():
    current_state = GPIO.input(26)
    GPIO.output(26, not current_state)
    print("Backlight toggled!")

print("Press the button connected to GPIO 16 to toggle the backlight.")
print("Fan is running... Enjoy the breeze!")

try:
    while True:
        # Check for button press (when button goes from HIGH to LOW)
        if GPIO.input(16) == GPIO.LOW:
            toggle_backlight()
            # Wait for the button to be released to avoid multiple toggles
            while GPIO.input(16) == GPIO.LOW:
                time.sleep(0.1)
            # Wait a bit after the button is released for debounce
            time.sleep(0.3)
        else:
            # Small delay to reduce CPU usage when button is not pressed
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\nShutting down, turning fan off...")
    GPIO.output(4, GPIO.LOW)  # Turn fan off
    GPIO.cleanup()  # Clean up GPIO on script exit
