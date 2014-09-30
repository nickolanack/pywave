#! /usr/bin/python
import sys
import wave
import audioop
import os

wavefile=sys.argv[1]
samples=int(sys.argv[2])
if(os.path.exists(wavefile)):
    h=wave.open(wavefile, 'r');
    for i in range(samples):
        a=h.readframes(h.getnframes()/samples);
        w=h.getsampwidth()*h.getnchannels();
        o=audioop.rms(a,w);
        print(o);
