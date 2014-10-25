#! /usr/bin/python
import sys
import wave
import audioop
import os

# this script prints the rms value (audio power) of an entire audio file. 
# this requires .wav files...
# execute: python waverms.py file.mp3 1024

wavefile=sys.argv[1]
samples=int(sys.argv[2])
if(os.path.exists(wavefile)):
    h=wave.open(wavefile, 'r');
    for i in range(samples):
        a=h.readframes(h.getnframes()/samples);
        w=h.getsampwidth()*h.getnchannels();
        o=audioop.rms(a,w);
        print(o);
