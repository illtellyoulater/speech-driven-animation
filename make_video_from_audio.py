import sda
import scipy.io.wavfile as wav
from PIL import Image
va = sda.VideoAnimator(gpu=0)# Instantiate the aminator
fs, audio_clip = wav.read("example/audio.wav")
frame = Image.open("example/image.bmp")
frame = "example/image.bmp"
vid, aud = va(frame, audio_clip, fs=fs)
va.save_video(vid, aud, "generated.mp4")
