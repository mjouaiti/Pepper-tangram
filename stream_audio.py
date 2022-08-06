import pyaudio
import numpy as np
import simpleaudio as sa
import wave
from scipy.io.wavfile import write

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 2048

audio = pyaudio.PyAudio()
info = audio.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

all_audio = []

for i in range(0, numdevices):
    if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", audio.get_device_info_by_host_api_device_index(0, i).get('name'))
        

def callback(input_data, frame_count, time_info, flags):
    global raw_audio#, wave0
    raw_audio = np.frombuffer(input_data, dtype=np.int16)
    play_obj = sa.play_buffer(raw_audio, 1, 2, RATE)
#    play_obj.wait_done()
#    all_audio.append(raw_audio)
#    wave0.writeframes(raw_audio)
    return raw_audio, pyaudio.paContinue

stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    stream_callback=callback,
                    frames_per_buffer=CHUNK,
                    input_device_index=0)

stream.start_stream()

#wave0=wave.open("mic.wav",'rb')
#wave0.setparams((CHANNELS, CHUNK, RATE, nframes, comptype, compname))

import time
while stream.is_active():
    pass
    
write("mic.wav", RATE, all_audio)

stream.stop_stream()
stream.close()
audio.terminate()
