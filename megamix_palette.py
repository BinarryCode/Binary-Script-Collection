# usage: python megamix_palette.py (filename)
# only has 1 argument for now.

# imports
from PIL import Image
import numpy as np
import sys
import os
# colors
white2 = (248,248,248,255) # eyes
skin = (248,224,160,255) # skin
primary = (0,112,232,255) # primary color - blue
secondary = (56,184,248,255) # secondary color - cyan
outline = (0,0,0,255) # outline color - black
# everything else
white = (255,255,255,255)
sorrynothing = (0,0,0,0)
img = Image.open('test.png')
width = img.size[0] 
height = img.size[1]
filename = sys.argv[1]
filenamePNGReduct = filename[:- 4]
pall_array = ["_primary.png", "_secondary.png", "_outline.png"]
#filenamePNGReduct = os.path.basename(filename)
# primary 
for times in range(3):
	img = Image.open(str(filename))
	for i in range(0,width):# process all pixels
		for j in range(0,height):
			data = img.getpixel((i,j))
			# mandatory colors removed
			if data == white2 :
				img.putpixel((i,j),sorrynothing)
			elif data == skin :
				img.putpixel((i,j),sorrynothing)
			# everything else!
			elif data == primary :
				if(times == 0):
					img.putpixel((i,j),white)
				else:
					img.putpixel((i,j),sorrynothing)
			elif data == secondary :
				if(times == 1):
					img.putpixel((i,j),white)
				else:
					img.putpixel((i,j),sorrynothing)
			elif data == outline :
				if(times == 2):
					img.putpixel((i,j),white)
				else:
					img.putpixel((i,j),sorrynothing)
			else:
				img.putpixel((i,j),sorrynothing)
	img.save(filenamePNGReduct + pall_array[times])