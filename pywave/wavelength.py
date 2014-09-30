#! /usr/bin/python
import sys
import wave
import os

wavefile=sys.argv[1]
if(os.path.exists(wavefile)):
    h=wave.open(wavefile, 'r');
    seconds=(h.getnframes()/h.getframerate());
    minutes=int(seconds/60.00);
    seconds=int(seconds%60);
    if(seconds<10):
        seconds="0"+str(seconds);
    time=str(minutes)+':'+str(seconds);
    print(time);
