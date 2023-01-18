%% This section takes care of merging any two .wav files

clc;
close all;
clear all;
cd ('/Users/talelzakhama/Box Sync/PeaqTestFiles/Rec/AAC-LC/LongDLRec/B188_AAC-LC_All_Peaq_Test_Files_W_Pads_And_Sines_Step_16');
% Put your sentence here
[recorded_wav, recorded_Fs] = audioread('Left_B188_AAC-LC_All_Peaq_Test_Files_W_Pads_And_Sines_Step_16.wav');
cd ('/Users/talelzakhama/Box Sync/Background Noise Files/Binaural');
[Noise_wav, Noise_FS] = audioread('Cafeteria_Noise_binaural ( 0.00-30.00 s).wav');

cd ('/Users/talelzakhama/Box Sync/PeaqTestFiles/Rec/AAC-LC/LongDLRec/Merging');
% audiowrite ('yo.wav',Noise_wav(1:min (length(Noise_wav),length(recorded_wav)))+recorded_wav(1:min (length(Noise_wav)...
%     ,length(recorded_wav))),recorded_Fs);
audiowrite ('yo.wav',Noise_wav((1:min(length(recorded_wav),length(Noise_wav))),1)+recorded_wav(1:min(length(recorded_wav),length(Noise_wav))),recorded_Fs);



%%
%############################%%             Concatenating .wav file, Stretching      #####################################################


% This portion is to make short noise files long
clc;
clear all;
close all;

cd ('/Users/talelzakhama/Box Sync/PeaqTestFiles/Rec/AAC-LC/LongDLRec/B188_AAC-LC_All_Peaq_Test_Files_W_Pads_And_Sines_Step_16');
[recorded_wav,Recorded_Fs] = audioread('Left_B188_AAC-LC_All_Peaq_Test_Files_W_Pads_And_Sines_Step_16.wav');

cd ('/Users/talelzakhama/Box Sync/Background Noise Files/Binaural');
Noise_Files=dir('*.wav');

mkdir Binaural_Long

% Bucket = zeros (length(recorded_wav),1);
for i=1:length(Noise_Files)
  cd ('/Users/talelzakhama/Box Sync/Background Noise Files/Binaural');
    [Noise_wav, Noise_FS] = audioread(sprintf(Noise_Files(i).name));
      s = 1;
    for j=1:length(recorded_wav)
     
        Bucket (j,1) = Noise_wav(s,2);
        
        s = s+1;
        
        if s == length(Noise_wav)
             s = 1;
        end
     
        
    end
cd ('/Users/talelzakhama/Box Sync/Background Noise Files/Binaural/Binaural_Long');
    audiowrite (sprintf('Long%s',Noise_Files(i).name),Bucket,Recorded_Fs);
end


%%
clc;
clear all;
close all;
cd ('/Users/talelzakhama/Box Sync/Background Noise Files/Binaural');
Noise_Files=dir('*.wav');
% for k=1:length(Noise_Files)
%        Noise_FileNames = Noise_Files(k).name;
% end
cd ('/Users/talelzakhama/Box Sync/PeaqTestFiles/Rec/AAC-LC/LongDLRec/B188_AAC-LC_All_Peaq_Test_Files_W_Pads_And_Sines_Step_16');
[recorded_wav, recorded_Fs] = audioread('Left_B188_AAC-LC_All_Peaq_Test_Files_W_Pads_And_Sines_Step_16.wav');





% rmdir Noise+Left
mkdir Noise+Left
cd ('/Users/talelzakhama/Box Sync/PeaqTestFiles/Rec/AAC-LC/LongDLRec/B188_All_Peaq_Test_Files_AAC-LC_Step16/Noise+Left')

for i=1:length(Noise_Files)
    Noise_FileNames = Noise_Files(i).name;
    cd ('/Users/talelzakhama/Box Sync/Background Noise Files/Binaural');
    [Noise_wav, Noise_FS] = audioread(sprintf(Noise_Files(i).name));
        
    cd ('/Users/talelzakhama/Box Sync/PeaqTestFiles/Rec/AAC-LC/LongDLRec/B188_AAC-LC_All_Peaq_Test_Files_W_Pads_And_Sines_Step_16/Noise+Left');
    audiowrite (sprintf('Left_%s',Noise_FileNames),Noise_wav((1:min(length(recorded_wav),length(long_noise_wav))),1)+recorded_wav(1:min(length(recorded_wav),length(long_noise_wav))),...
        recorded_Fs);

end
i




