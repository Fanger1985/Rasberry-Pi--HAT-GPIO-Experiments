import RPi.GPIO as GPIO
import time

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)  # TFT backlight
GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)   # Fan control, start HIGH (fan on)
GPIO.setup(16, GPIO.IN)                      # Button for backlight toggle

# Function to toggle the backlight
def toggle_backlight():
    current_state = GPIO.input(26)
    GPIO.output(26, not current_state)
    print("Backlight toggled!")

print("Press the button connected to GPIO 16 to toggle the backlight.")
print("Fan is running... Enjoy the breeze!")

# Variable to keep track of the last button state to detect changes
last_button_state = GPIO.input(16)

try:
    while True:
        # Read the button state
        current_button_state = GPIO.input(16)
        
        # Check if button state has changed from high to low
        if current_button_state == GPIO.LOW and last_button_state == GPIO.HIGH:
            toggle_backlight()
            time.sleep(0.3)  # Debounce delay

        # Update the last button state
        last_button_state = current_button_state

        time.sleep(0.1)  # Small delay to reduce CPU usage

except KeyboardInterrupt:
    print("\nShutting down, turning fan off...")
    GPIO.output(4, GPIO.LOW)  # Turn fan off
    GPIO.cleanup()  # Clean up GPIO on script exit
