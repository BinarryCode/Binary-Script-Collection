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

# Put Offset lines below here
