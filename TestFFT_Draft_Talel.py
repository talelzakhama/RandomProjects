
import Audio.AudioAnalyzer as AA
import os
import soundfile as sf

if __name__ == '__main__':
	chan_1_file = "/Users/talelmacbookpro2/Documents/Source_wav_files/Speech_Far_End_Vol_Steps.wav"
	# chan_1_file = "/Users/davidgarber/Band_Limited_Pink_Noise.wav"
	print (chan_1_file)
	print ('\n\n') 
	fft_spectrum = AA.getFFTAverage(chan_1_file)
	RMS_Power = AA.getRmsPowerCurve(20, chan_1_file)
	AA.plotOneFFTSpectrum(fft_spectrum, os.path.dirname(chan_1_file))