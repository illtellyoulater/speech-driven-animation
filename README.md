# Speech-Driven Animation

This library implements the end-to-end facial synthesis model described in this [paper](https://sites.google.com/view/facialsynthesis/home).

![speech-driven-animation](example.gif)

## Downloading the models
The models were hosted on git LFS. However the demand was so high that I reached the quota for free gitLFS storage. I have moved the models to GoogleDrive. Models can be found [here](https://drive.google.com/drive/folders/17Dc2keVoNSrlrOdLL3kXdM8wjb20zkbF?usp=sharing).
Place the model file(s) under sda/data/

## Installing

conda create -n sda

conda activate sda

conda install python=3.9

Then install the following packages

Name, Version, Channel

blas                      1.0                         

blosc                     1.21.0               

brotli                    1.0.9                

bzip2                     1.0.8                

ca-certificates           2021.10.26           

certifi                   2021.10.8        

cfitsio                   3.470                

charls                    2.2.0                

cloudpickle               2.0.0              

colorama                  0.4.4                        pypi

cudatoolkit               11.3.1               

cycler                    0.11.0             

cytoolz                   0.11.0           

dask-core                 2021.10.0          

face-alignment            1.3.5                        pypi

ffmpeg                    2.7.0                        menpo

ffmpeg-python             0.2.0                        pypi

fonttools                 4.25.0             

freetype                  2.10.4               

fsspec                    2021.10.1          

future                    0.18.2                       pypi

giflib                    5.2.1                

icc_rt                    2019.0.0             

imagecodecs               2021.8.26        

imageio                   2.9.0              

intel-openmp              2021.4.0          

jpeg                      9d                   

kiwisolver                1.3.1            

lcms2                     2.12                 

lerc                      3.0                  

libaec                    1.0.4                

libdeflate                1.8                  

libpng                    1.6.37               

libtiff                   4.2.0                

libuv                     1.40.0               

libwebp                   1.2.0                

libzopfli                 1.0.3                

llvmlite                  0.37.0                       pypi

locket                    0.2.1            

lz4-c                     1.9.3                

matplotlib-base           3.5.0            

mkl                       2021.4.0           

mkl-service               2.4.0            

mkl_fft                   1.3.1            

mkl_random                1.2.2            

munkres                   1.1.4                      

networkx                  2.6.3              

numba                     0.54.1                       pypi

numpy                     1.20.3                       pypi

olefile                   0.46               

opencv-python             4.5.4.60                     pypi

openjpeg                  2.4.0                

openssl                   1.1.1l               

packaging                 21.3               

partd                     1.2.0              

pillow                    8.4.0            

pip                       21.2.4           

pydub                     0.25.1                       pypi

pyee                      8.2.2                        pypi

pyparsing                 3.0.4              

python                    3.9.7                

python-dateutil           2.8.2              

pytorch                   1.10.0                       pytorch

pytorch-mutex             1.0                          pytorch

pywavelets                1.1.1            

pyyaml                    6.0              

scikit-image              0.18.3           

scikit-video              1.1.11                       pypi

scipy                     1.7.1            

setuptools                58.0.4           

six                       1.16.0             

snappy                    1.1.8                

sqlite                    3.36.0               

tifffile                  2021.7.2           

tk                        8.6.11               

toolz                     0.11.2             

torchaudio                0.10.0                      pytorch

torchvision               0.11.1                      pytorch

tqdm                      4.62.3                      pypi

typing_extensions         3.10.0.2           

tzdata                    2021e                

vc                        14.2                 

vs2015_runtime            14.27.29016          

wheel                     0.37.0             

wincertstore              0.2              

xz                        5.2.5                

yaml                      0.2.5                

zfp                       0.5.5                

zlib                      1.2.11               

zstd                      1.4.9                


## Running the example

To create the animations you will need to instantiate the VideoAnimator class. Then you provide an image and audio clip (or the paths to the files) and a video will be produced.

## Choosing the model
The model has been trained on the GRID, TCD-TIMIT, CREMA-D and LRW datasets. The default model is GRID. To load another pretrained model simply instantiate the VideoAnimator with the following arguments:

```
import sda
va = sda.VideoAnimator(gpu=0, model_path="crema")# Instantiate the animator
```

The models that are currently uploaded are:
- [x] grid
- [x] timit
- [x] crema
- [ ] lrw

### Example with Numpy Arrays
```
import sda
import scipy.io.wavfile as wav
from PIL import Image
va = sda.VideoAnimator(gpu=0)# Instantiate the aminator
fs, audio_clip = wav.read("example/audio.wav")
frame = Image.open("example/image.bmp")
frame = "example/image.bmp"
vid, aud = va(frame, audio_clip, fs=fs)
va.save_video(vid, aud, "generated.mp4")

## Using the encodings
The encoders for audio and video are made available so that they can be used to produce features for classification tasks.

### Audio Encoder
The Audio Encoder (which is made of Audio-Frame encoder and RNN) is provided along with a dictionary which has information such as the feature length (in seconds) required by the Audio Frame encoder and the overlap between audio frames.
```
import sda
encoder, info = sda.get_audio_feature_extractor(gpu=0)
```

### See README.md.old for different install approaches and examples (which didn't work for me)
