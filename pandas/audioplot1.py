import wave
import matplotlib.pyplot as plt

input_data = wave.open('abcd1.wav','r')
audio = input_data[1]
plt.plot(audio[0:1024])
plt.ylabel("Amplitude")
plt.xlabel("Time (samples)")
plt.title("Flute Sample")
plt.show()
