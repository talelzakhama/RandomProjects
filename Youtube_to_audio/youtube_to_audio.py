import pytube
from moviepy.editor import *

#Prerequisite:
# Install ffmpeg from the following link:
# https://www.ffmpeg.org/download.html

# Enter the URL of the YouTube video you want to convert
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Download the YouTube video
youtube = pytube.YouTube(video_url)
video = youtube.streams.get_highest_resolution()
video.download(filename='video')

# Convert the downloaded video to audio
video_path = "video.mp4"
audio_path = "~/Downloads/audio.mp3"

video_clip = VideoFileClip(video_path)
video_clip.audio.write_audiofile(audio_path)

# Remove the video file
video_clip.close()
os.remove(video_path)

print("Conversion complete!")
