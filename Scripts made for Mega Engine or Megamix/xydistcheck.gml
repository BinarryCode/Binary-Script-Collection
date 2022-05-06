/// xydistcheck(axis, target_obj)
// Returns distance. (axis is 0 for x, 1 for y)
// target should usually be objMegaman.

if(instance_exists(argument1))
{
    if(argument0 == 0)
        return abs(x - argument1.x);
    else if(argument0 == 1)
        return abs(y - argument1.y);
} else
    return 0;