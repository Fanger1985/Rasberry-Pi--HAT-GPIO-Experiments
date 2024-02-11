import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS, DC, and RESET pins:
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# SPI and ST7789 display initialization:
spi = board.SPI()
display = st7789.ST7789(spi, rotation=180, cs=cs_pin, dc=dc_pin, rst=reset_pin, width=240, height=240, baudrate=24000000)

# Create an image with a white background:
image = Image.new("RGB", (240, 240), "white")
draw = ImageDraw.Draw(image)

# Load a font:
font = ImageFont.load_default()  # Using the default font as a fallback

# Define text and calculate approximate text size:
text = "Hello, World!"
approximate_font_size = 10  # Approximation for the default font size
text_width = approximate_font_size * len(text)  # Rough approximation of text width
text_height = approximate_font_size  # Rough approximation of text height

# Calculate text position for centering:
x = (240 - text_width) / 2
y = (240 - text_height) / 2

# Draw the text:
draw.text((x, y), text, font=font, fill="black")

# Display the image on the TFT screen:
display.image(image)
