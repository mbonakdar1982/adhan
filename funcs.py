from pygame import mixer
import time
import os
import random
import eyed3


def segment(filePath, mode='random'):
    from pydub import AudioSegment
    from pydub.silence import split_on_silence
    
    
    sound = AudioSegment.from_mp3(filePath)
    length = int(len(sound) / 1000)
    print(length)
    #audio_chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-40 )
    if mode == 'random':
        first10min = sound[:20000]
        first10min.export("first10min.mp3", format="mp3")
        '''
        for i, chunk in enumerate(audio_chunks):
            output_file = "chunk{0}.mp3".format(i)
            print("Exporting file", output_file)
            chunk.export(output_file, format="mp3")
        '''
        #secondHalf = sound[int(length / 2) : ]
        #secondHalf.export("Friday_secondHalf.mp3", format="mp3")
    elif mode == 'all':

        pass
    else:
        pass

    return None
        




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
    #playdoa('eftetah_fani_1')
    #playdoa('eftetah_fani_2')
    segment('assets/quran/sudais/005.mp3')