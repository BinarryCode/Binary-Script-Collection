import os
import sys

print("Danimator Un-Fuck-Up Script")
print("Made by Binrary#6656")
print("Because the developer didn't open-source it.")
print("To use, edit the bottom of this file to contain offsets formatted as so:")
print("Offset(X, Y, SpriteX, SpriteY)")
print("X and Y should be the same as it is in Danimator.")
print("SpriteX and SpriteY should be the same as they are in SLADE.")

def Offset(movedX, movedY, spriteX, spriteY):
	finalX = (movedX + spriteX)
	finalY = (movedY + spriteY)
	print("Offset(" + str(finalX) + ", " + str(finalY) + ")")

# Wekapipo Mainfire Example
# First two arguments are from Danimator.
# Last two arguments are from SLADE.
'''
WKAR A 1 Offset(170, 83)
WKAR C 1 Offset(184, 58)
WKAR C 1 Offset(194, 49)
WKAR C 1 Offset(202, 40)
WKAR C 1 Offset(210, 31)
WKAR D 1 Offset(214, 31)
WKAR D 1 Offset(198, 39)
WKAR D 1 Offset(172, 57)
WKAR E 1 Offset(155, 126)
WKAR E 1 Offset(150, 135)
WKAR E 1 Offset(139, 148)
'''
Offset(170, 83, -170, -83)
Offset(184, 58, -170, -83)
Offset(194, 49, -170, -83)
Offset(202, 40, -170, -83)
Offset(210, 31, -170, -83)
Offset(214, 31, -174, -83)
Offset(198, 39, -174, -83)
Offset(172, 57, -174, -83)
Offset(155, 126, -165, -142)
Offset(150, 135, -165, -142)
Offset(139, 148, -165, -142)

# Dr. Jekyll M1 Example
# Same as above.
'''Offset(163, 81, -163, -81)
Offset(169, 66, -164, -59)
Offset(174, 61, -164, -59)
Offset(180, 58, -164, -59)
Offset(200, 37, -155, -51)
Offset(205, 35, -155, -51)
'''
