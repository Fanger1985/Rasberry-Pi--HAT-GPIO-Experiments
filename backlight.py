import RPi.GPIO as GPIO
import keyboard

# Set up the GPIO pin
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)  # Set GPIO 26 as output, start HIGH (backlight on)

def toggle_backlight():
    current_state = GPIO.input(26)
    GPIO.output(26, not current_state)

# Main loop
print("Press 'b' to toggle the backlight.")
while True:
    try:
        if keyboard.is_pressed('b'):  # If 'b' is pressed
            toggle_backlight()
            while keyboard.is_pressed('b'):  # Wait for 'b' to be released
                pass
    except KeyboardInterrupt:
        break

GPIO.cleanup()  # Clean up GPIO on normal exit
