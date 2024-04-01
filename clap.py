import sounddevice as sd
import numpy as np
threshold =2.5
clap = False
def detect_clap(indata,frames,time,status):
    global clap
    volume_norm=np.linalg.norm(indata)*10
    if volume_norm>threshold:
        print("clapped true ")
        clap=True

def Listen_for_claps():
    with sd.InputStream(callback=detect_clap):
        return sd.sleep(1000)

def mainclap():
    while True:
        Listen_for_claps()
        if clap==True:
            break
        else:
            pass

