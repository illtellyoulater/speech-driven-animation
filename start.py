
import os
import sda
import scipy.io.wavfile as wav
from PIL import Image
from datetime import datetime


os.system("cls")
print("This will generate a video of a person speaking, based on a single photo of that person and an audio file.\n")
print("Media should be placed in the /example folder.\n")

print("What's the name of the image file? (e.g. 'person.jpg')")
image_file_name = input()
print("What's the name of the audio file? (e.g. 'audio.mp3')")
audio_file_name = input()
print("\nWorking...\n")

va = sda.VideoAnimator(gpu=0, model_path="grid") # Instantiate the animator(gpu, model_path)
fs, audio_clip = wav.read("example/" + audio_file_name)
frame = Image.open("example/" + image_file_name)
frame = "example/" + image_file_name
vid, aud = va(frame, audio_clip, fs=fs)
va.save_video(vid, aud, "generated" +  datetime.now().strftime("%d-%m-%Y--%H-%M-%S") +".mp4")


print("Done!\n")