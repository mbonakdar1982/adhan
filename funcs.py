from pygame import mixer
import time
import os
import random
#import eyed3
import re
import subprocess
from radio import radio_channels
import vlc



SPEAKER_MAC = "90:F2:60:15:2E:2E"
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
        options = list(set([re.sub(r'[0-9]', '', filename[:-4]) for filename in os.listdir('assets/doa/') if 'doa' in filename]))
        print(options)
        selectedOption = random.choice(options) 
        print('selected option: {}'.format(selectedOption))
        doaFiles = ['assets/doa/' + f for f in os.listdir('assets/doa/') if selectedOption in f]
        doaFiles.sort()
        print('files to be played: {}'.format(doaFiles))

    else:
        options = [filename for filename in os.listdir('assets/doa/') if doa in filename]
        doaFiles = ['assets/doa/' + f for f in os.listdir('assets/doa/') if f in options]
        doaFiles.sort()
        print(doaFiles)
   
    mixer.init()
    for doaFile in doaFiles:
        sound = mixer.Sound(doaFile)
        length = sound.get_length()
        print(doaFile)
        print(length)
        sound.play()
        time.sleep(length if duration == 0 else duration * 60)
    return 'OK'

def playRadio(channel, duration):
    player = vlc.MediaPlayer(radio_channels[channel])
    player.play()
    time.sleep(duration)
    player.stop()
    return "OK"


def run_cmd(cmd):
    """Run a shell command and return output."""
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

def bluetoothctl_command(command):
    """Send command to bluetoothctl."""
    return run_cmd(f'echo -e "{command}" | bluetoothctl')

def connect_speaker(mac):
    print("Turning on Bluetooth agent...")
    bluetoothctl_command("power on")
    bluetoothctl_command("agent on")
    bluetoothctl_command("default-agent")

    print("Scanning for devices...")
    bluetoothctl_command("scan on")
    time.sleep(5)
    bluetoothctl_command("scan off")

    print(f"Pairing with {mac}...")
    bluetoothctl_command(f"pair {mac}")
    time.sleep(2)

    print(f"Trusting {mac}...")
    bluetoothctl_command(f"trust {mac}")
    time.sleep(1)

    print(f"Connecting to {mac}...")
    bluetoothctl_command(f"connect {mac}")
    time.sleep(3)

    print("Setting speaker as default audio sink...")
    subprocess.run(["pactl", "set-default-sink", mac.replace(":", "_") + ".a2dp_sink"])

    print("Done. Audio should now play through the Bluetooth speaker.")






if __name__ == '__main__':
    #playdoa('Monday')
    subprocess.run(["pactl", "set-default-sink", SPEAKER_MAC.replace(":", "_") + ".a2dp_sink"])
    