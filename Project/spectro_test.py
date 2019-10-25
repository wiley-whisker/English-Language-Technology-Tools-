from scipy.io import wavfile
import matplotlib.pyplot as plot

# Read the wav file (mono)

wav_file = 'data/test.wav'

samplingFrequency, signalData = wavfile.read(wav_file)

# Plot the signal read from wav file

plot.subplot(211)

plot.title(wav_file)

plot.plot(signalData)

plot.xlabel('Sample')

plot.ylabel('Amplitude')

plot.subplot(212)

plot.specgram(signalData, Fs=samplingFrequency)

plot.xlabel('Time')

plot.ylabel('Frequency')

plot.show()