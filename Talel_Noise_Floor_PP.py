from __future__ import print_function
import sounddevice as sd
from matplotlib import rc
import AudioTools.AudioAnalyzer as AA
import AudioTools.AudioAnalyzer as analyzer
import os
import sys
import soundfile as sf
import BeatsTests.Audio.A2dpAudioDetection

print(BeatsTests.Audio.A2dpAudioDetection.__file__)
from BeatsTests.Audio.A2dpAudioDetection import noiseFloorPostProcessinggg
import unicodedata
from BeatsSources.AppleDevice import AppleDevice
from time import time, sleep
import pyaudio

if __name__ == '__main__':
    source = AppleDevice()
    source.playSong("Silence")
    source.setVolume(16)
    source.pause()

    reference_wav_file = input("\nEnter the path of the reference file:\n").strip()

    noise_floor_wav_file = noiseFloorPostProcessing(reference_wav_file)

    measurement_wav_file = input("\nEnter the path of the measurement wav file:\n").strip()

    noise_floor_measurement_wav_file = noiseFloorPostProcessing(measurement_wav_file)

    print(noise_floor_measurement_wav_file)

print("\n\n" + unicodedata.lookup("GREEK CAPITAL LETTER DELTA") + "_Noise_floor =",
      [element - noise_floor_wav_file[0] for element in noise_floor_measurement_wav_file], "dB\n\n")

