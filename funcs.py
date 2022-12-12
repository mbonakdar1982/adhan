from pygame import mixer
import time
import os
import random
import eyed3


def playAdhan():
    options = os.listdir('assets/adhan/')
    adhanFile = 'assets/adhan/' + random.choice(options)
    print(adhanFile)
    mixer.init()
    sound = mixer.Sound(adhanFile)
    length = sound.get_length()
    sound.play()
    time.sleep(length)
    return 'OK'

def playQuran(duration):
    #surah = random.choice(list(range(1,115)))
    options = os.listdir('assets/quran/')
    quranFile = 'assets/quran/' + random.choice(options)
    print(quranFile)
    mixer.init()
    sound = mixer.Sound(quranFile)
    length = sound.get_length()
    sound.play()
    time.sleep(duration)
    return 'OK'

def playsound(what, duration = 0):
    mixer.init()
    FilePath = 'assets/sounds/' + what + '.mp3'
    sound = mixer.Sound(FilePath)
    length = sound.get_length()
    if duration == 0:
        duration = length
    sound.play()
    time.sleep(duration)

def playdoa(doa='random', duration=0):
    if doa == 'random':
        options = os.listdir('assets/doa/')
    else:
        options = [file for file in os.listdir('assets/doa/') if doa in file ]
    doaFile = 'assets/doa/' + random.choice(options)  
    print(doaFile)  

    mixer.init()
    sound = mixer.Sound(doaFile)
    length = sound.get_length()
    print(length)
    sound.play()
    time.sleep(length if duration == 0 else duration * 60)
    return 'OK'

if __name__ == '__main__':
    playdoa('Friday')
    playdoa('komeyl')