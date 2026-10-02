import math
import random
import struct
import wave

samplerate = 44100

left_channel = [
    0.5 * math.sin(2 * math.pi * 440.0 * i / samplerate) for i in range(samplerate)
]
right_channel = [random.random() for _ in range(samplerate)]

with wave.open("sound2.wav", "w") as f:
    f.setnchannels(2)
    f.setsampwidth(2)
    f.setframerate(samplerate)
    for samples in zip(left_channel, right_channel):
        for sample in samples:
            sample = int(sample * (2 ** 15 - 1))
            f.writeframes(struct.pack("<h", sample))