/// needleXYDistCheck(target)
// Returns distance, used for Needleman's needle-firing attack.

if(instance_exists(argument0))
{
    if (xydistcheck(0,argument0) >= xydistcheck(1,argument0))
        return 1;
    else
        return 0;
} else
    return 0;