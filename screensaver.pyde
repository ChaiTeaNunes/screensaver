# Copyright (c) Chai Nunes
FPS = 10
PER_FRAME = 1
B_DIFF = -30
NUM_CIRCLES = 3

def setup():
    fullScreen()
    background(0)
    frameRate(FPS)
    strokeWeight(0)

def draw():
    for _ in range(0, PER_FRAME):
        randx, randy = random(width), random(height) # Generate random x and y positions
    
        colorMode(RGB) # Change mode for color
        r = abs(randx - (width - randx)) / width * 255 # Further from the center on the x-axis is more red
        b = abs(randy - (height - randy)) / height * 255 # Further from the center on the y-axis is more blue
        g = 255 - (r + b) # Close to the center is more green
        c = color(r, g, b) # Set default color
    
        colorMode(HSB) # Change mode for darkness
        for i in range(NUM_CIRCLES, 0, -1):
            fill(c)
            ellipse(randx, randy, i  * int(100 / NUM_CIRCLES), i * int(100 / NUM_CIRCLES)) # Create inner circles
            c = color(hue(c), saturation(c), brightness(c) + B_DIFF) # Darken
