# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import random 
 
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D12
 
# The number of NeoPixels
num_pixels = 100
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
 
 
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)
 
 
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def randomColor():
	color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
	return color

def strobe(pixelSetting,delay,numLoops):
	for i in range(numLoops):
		pixelsTemp = pixelSetting[:]
		pixelSetting.show()
		time.sleep(delay)
		pixelSetting.fill((0,0,0))
		pixelSetting.show()
		time.sleep(delay)
		pixelSetting = pixelsTemp[:]
	return pixelSetting

#def brightnessLevel(brightness, color):
#	color = ((brightness*color[0])//1,(brightness*color[1])//1,(brightness*color[2])//1)
#	return color

def test1(wait):
	
	for j in range(255):
		step = 2
		for i in range(0,num_pixels,step):
			pixel_index = (i * 256 // num_pixels) + j
			pixels[i] = wheel(pixel_index & 255)
		pixels.show()
		time.sleep(wait*10)
		pixels.fill((0,0,0))
		pixels.show()
		time.sleep(wait)

def  barFill(wait):
	pixels.fill((0,0,0))
	pixels.show()
	pixels[0] = (randomColor())
	pixels.show()
	for i in range(num_pixels-1):
		pixels[i+1] = (randomColor())
		pixels.show()
		time.sleep(wait)

def  meetInMiddle(wait):
	pixels.fill((0,0,0))
	pixels.show()
	for i in range(num_pixels//2):
		pixels[i] = (255,0,0)
		pixels[num_pixels-1-i] = (10,0,0)
		pixels.show()
		time.sleep(wait)
	for i in range(num_pixels//2):
		pixels[num_pixels//2+i] = (0,0,0)
		pixels[num_pixels//2-1-i] = (0,0,0)
		pixels.show()
		time.sleep(wait)

def  growFromMiddle(wait):
	pixels.fill((0,0,0))
	pixels.show()
	for i in range(num_pixels//2):
		pixels[num_pixels//2+i] = (randomColor())
		pixels[num_pixels//2-1-i] = (randomColor())
		pixels.show()
		time.sleep(wait)

def  snake(wait):
	pixels.show()
	for i in range(num_pixels):
		pixels.fill(randomColor())
		pixels[i] = (0,0,0)
		pixels.show()
		time.sleep(wait)

def rain():
	pixels.fill((0,0,0))
	pixels.show()
	for i in range(0,random.randint(1,20)):
		pixels[random.randint(0,num_pixels-1)] = (0,205,0)
	pixels.show()
	time.sleep(0.25)

def copLights():
	for i in range(0,num_pixels//2):
		pixels[i] = (255,0,0)
	strobe(pixels,0.05,3)
	pixels.show()
	pixels.fill((0,0,0))
	time.sleep(0.1)
	for i in range(num_pixels//2,num_pixels):
		pixels[i] = (0,255,0)
	strobe(pixels,0.05,3)
	pixels.show()
	pixels.fill((0,0,0))
	time.sleep(0.1)	



 
while True:
    # Comment this line out if you have RGBW/GRBW NeoPixels
   # pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
   # pixels.show()
    #time.sleep(1)
 
    # Comment this line out if you have RGBW/GRBW NeoPixels
   # pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
   # pixels.show()
   # time.sleep(1)
 
    # Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    #pixels.show()
    #time.sleep(1)
 
#    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
#	meetInMiddle(.1)
#	rain()
    copLights()
#	pixels.fill((0,255,0))
#	pixels.show()
#	strobe(pixels,.1)
	
