# "Binary's Script Collection"
## A collection of scripts that I have made.
If there are any issues, please do a issue or pull request.

Note that you will need to manually edit these scripts a bit after downloading them, but there's not much I can do about that.

# Danimator-UnFuckUp-Script
## Made for use with [Danimator](https://forum.zdoom.org/viewtopic.php?t=49494)!
## Instructions
* Edit the bottom of the Python script to contain offsets formatted as so:
`
Offset(X, Y, SpriteX, SpriteY)
`
  * `X` and `Y` should be the same as they are in Danimator.
  * `SpriteX` and `SpriteY` should be the same as the sprite offsets in [SLADE](https://slade.mancubus.net/index.php?page=downloads).
* Then, run the script. You should be able to copy the offsets for use with the PK3.

# Megamix-Palette.py
## Made for use with [Megamix Engine](https://magmmlcontest.com/megamix.php), but can be used with [Mega Engine](https://www.sprites-inc.co.uk/thread-1648.html) as well.
## Instructions
* Edit the top of the Python script to include proper character colors if needed.
* Install the requirements (NumPy, Pillow/PIL)
* Then, run the script as so, replacing "(filename)" with your filename:
`
Python Megamix_Palette.py (filename)
`
