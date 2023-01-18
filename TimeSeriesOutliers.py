# This is where you get TimeSynth from:
# !pip install git+https://github.com/TimeSynth/TimeSynth.git
# Reference: https://docs.seldon.io/projects/alibi-detect/en/stable/examples/od_sr_synth.html
import timesynth as ts
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, recall_score
import matplotlib.pyplot as plt
import librosa.display
from alibi_detect.od import SpectralResidual
from alibi_detect.utils.perturbation import inject_outlier_ts
from alibi_detect.utils.saving import save_detector, load_detector
from alibi_detect.utils.visualize import plot_instance_score, plot_feature_outlier_ts
from sksound.sounds import Sound
import librosa
from prettytable import PrettyTable


audio_data = '/Users/talelzakhama/Desktop/Test_77542941_05_07_2021_16_29_48.wav'
x , sr = librosa.load(audio_data)
# print ('Sample rate is {}'.format(sr))
# print ('x is {}'.format(x))
print(type(x), type(sr))#<class 'numpy.ndarray'> <class 'int'>print(x.shape, sr)#(94316,) 22050
plt.figure(figsize=(14, 5))
librosa.display.waveplot(x, sr=sr)
plt.show()

od = SpectralResidual(
    threshold=1,  # threshold for outlier score
    window_amp=20,   # window for the average log amplitude
    window_local=20, # window for the average saliency map
    n_est_points=20  # nb of estimated points padded to the end of the sequence
)

od.infer_threshold(
    x,
    t=1//sr,  # array with timesteps, assumes dt=1 between observations if omitted
    threshold_perc=95
)

preds = od.predict(
    x,
    t=1//sr,  # array with timesteps, assumes dt=1 between observations if omitted
    return_instance_score=True
)

print (preds)