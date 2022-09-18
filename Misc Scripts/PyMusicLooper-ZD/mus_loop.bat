@echo off
FOR %%A IN (%*) DO (
    ECHO finding loop point for %%A...
    pymusiclooper %%A -t -n 1 --stdout -v
    ECHO exporting .ogg file as %%A_LOOP.ogg...
    python mus_loop.py %%A
)