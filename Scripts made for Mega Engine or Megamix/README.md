# Mega Engine/Megamix Scripts
## Made for use with [Megamix Engine](https://magmmlcontest.com/megamix.php), but can be used with [Mega Engine](https://www.sprites-inc.co.uk/thread-1648.html) as well.
## Any scripts that are not mine will not be given its own section.

# Python Scripts

# Megamix-Palette.py
## Made to help with whitemasking. ONLY WORKS WITH PNGS!
## Instructions
* Installed the following required packages:
```
pip install numpy
pip install pillow
```
* Edit the top of the Python script to include proper character colors if needed.
* Then, run the script as so, replacing "(filename)" with your filename:
```
Python Megamix_Palette.py (filename)
```

# GML Scripts

# fc_value(int,sub)
## Made to help with accurately recreating boss AI...if you know ASM.
## Credits to SokZaJelo for helping a bit with this script!
## Usage Example
```
jumpYValue[0] = fc_value($04,$9e);
jumpYValue[1] = fc_value($06,$88);
jumpYValue[2] = fc_value($08,$00);
jumpYValue[3] = fc_value($06,$88);
```
Shadow Man's jump values taken from [a MM3 Disassembly](https://github.com/refreshing-lemonade/megaman3-disassembly). (Shadowman's gravity is 0.33 instead of 0.25, which is why these values are a bit high.)

# xydistcheck(axis, target)
## A distance check that is more accurate to the source games, and used in the script below.
# mm4_distcheck(target, dist1, dist2)
## Made to help with accurately recreating MM4's boss AI, or for custom battles.
## Usage Example (uses chance.gml)
```
switch(mm4_distcheck(objMegaman, 64, 128))
{
    case 0:
        choosingJump = 62.5;
        choosingShoot = 37.5;
    break;
    case 1:
        choosingJump = 50;
        choosingShoot = 50;
    break;
    case 2:
        choosingJump = 37.5;
        choosingShoot = 62.5;
    break;
}
//Each of these values has a chance of happening.
if (chance(choosingJump))
{
    phase = 1;
    attackTimer = 0;
}
if (chance(choosingShoot))
{
    shotsFired = 0;
    event_user(1); //choose the actual bullet pattern.
    attackTimer = 0;
    phase = 2;
}
```
Bright Man's chances of using each attack, as shown in [this video](https://youtu.be/PME8HLPRCOI).

# needleXYDistCheck(target)
## Made specifically for Needle Man, but might be useful for other situations.
## Usage Example
```
    var projID;
    projID = instance_create(x+10*image_xscale,y+2,objNeedlemanCannon);
    projID.image_xscale = self.image_xscale;
    with(projID)
    {
        if instance_exists(objMegaman)
        {
            var angle;
            angle = point_direction(sprite_get_xcenter(), sprite_get_ycenter(), sprite_get_xcenter_object(objMegaman), sprite_get_ycenter_object(objMegaman));
            if(needleXYDistCheck(objMegaman))
            {
                if(objMegaman.x < x)
                    xspeed = -4;
                else
                    xspeed = 4;
                yspeed = -sin(degtorad(angle)) * 4;
            }
            else
            {
                xspeed = cos(degtorad(angle)) * 4;
                yspeed = 4;
            }
        }
        else
        {
            xspeed = 4 * image_xscale;
            yspeed = 0;
        }
    }
}
```
Needle Man's projectile being fired. It works like this in MM3.
