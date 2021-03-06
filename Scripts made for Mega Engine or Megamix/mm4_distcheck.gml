/// mm4_distcheck(target_obj, dist1, dist2)
// Returns either 0 for short, 1 for mid, or 2 for long.
// MM4 uses this for most of the bosses, hence the name of the script.
// target should usually be objMegaman.
if(instance_exists(argument0))
{
var dist;
dist = xydistcheck(0,argument0);
    if dist < argument1 //64
        return 0;
    else if dist < argument2 //128
        return 1;
    else
        return 2;
} else //A extra failsafe, uses pure RNG if the target doesn't exist at all.
    return choose(0,1,2);
