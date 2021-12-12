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

Install the following packages

# Name                    Version                   Build  Channel
blas                      1.0                         mkl
blosc                     1.21.0               h19a0ad4_0
brotli                    1.0.9                ha925a31_2
bzip2                     1.0.8                he774522_0
ca-certificates           2021.10.26           haa95532_2
certifi                   2021.10.8        py39haa95532_0
cfitsio                   3.470                he774522_6
charls                    2.2.0                h6c2663c_0
cloudpickle               2.0.0              pyhd3eb1b0_0
colorama                  0.4.4                    pypi_0    pypi
cudatoolkit               11.3.1               h59b6b97_2
cycler                    0.11.0             pyhd3eb1b0_0
cytoolz                   0.11.0           py39h2bbff1b_0
dask-core                 2021.10.0          pyhd3eb1b0_0
face-alignment            1.3.5                    pypi_0    pypi
ffmpeg                    2.7.0                         0    menpo
ffmpeg-python             0.2.0                    pypi_0    pypi
fonttools                 4.25.0             pyhd3eb1b0_0
freetype                  2.10.4               hd328e21_0
fsspec                    2021.10.1          pyhd3eb1b0_0
future                    0.18.2                   pypi_0    pypi
giflib                    5.2.1                h62dcd97_0
icc_rt                    2019.0.0             h0cc432a_1
imagecodecs               2021.8.26        py39ha1f97ea_0
imageio                   2.9.0              pyhd3eb1b0_0
intel-openmp              2021.4.0          haa95532_3556
jpeg                      9d                   h2bbff1b_0
kiwisolver                1.3.1            py39hd77b12b_0
lcms2                     2.12                 h83e58a3_0
lerc                      3.0                  hd77b12b_0
libaec                    1.0.4                h33f27b4_1
libdeflate                1.8                  h2bbff1b_5
libpng                    1.6.37               h2a8f88b_0
libtiff                   4.2.0                hd0e1b90_0
libuv                     1.40.0               he774522_0
libwebp                   1.2.0                h2bbff1b_0
libzopfli                 1.0.3                ha925a31_0
llvmlite                  0.37.0                   pypi_0    pypi
locket                    0.2.1            py39haa95532_1
lz4-c                     1.9.3                h2bbff1b_1
matplotlib-base           3.5.0            py39h6214cd6_0
mkl                       2021.4.0           haa95532_640
mkl-service               2.4.0            py39h2bbff1b_0
mkl_fft                   1.3.1            py39h277e83a_0
mkl_random                1.2.2            py39hf11a4ad_0
munkres                   1.1.4                      py_0
networkx                  2.6.3              pyhd3eb1b0_0
numba                     0.54.1                   pypi_0    pypi
numpy                     1.20.3                   pypi_0    pypi
olefile                   0.46               pyhd3eb1b0_0
opencv-python             4.5.4.60                 pypi_0    pypi
openjpeg                  2.4.0                h4fc8c34_0
openssl                   1.1.1l               h2bbff1b_0
packaging                 21.3               pyhd3eb1b0_0
partd                     1.2.0              pyhd3eb1b0_0
pillow                    8.4.0            py39hd45dc43_0
pip                       21.2.4           py39haa95532_0
pydub                     0.25.1                   pypi_0    pypi
pyee                      8.2.2                    pypi_0    pypi
pyparsing                 3.0.4              pyhd3eb1b0_0
python                    3.9.7                h6244533_1
python-dateutil           2.8.2              pyhd3eb1b0_0
pytorch                   1.10.0          py3.9_cuda11.3_cudnn8_0    pytorch
pytorch-mutex             1.0                        cuda    pytorch
pywavelets                1.1.1            py39h080aedc_4
pyyaml                    6.0              py39h2bbff1b_1
scikit-image              0.18.3           py39hf11a4ad_0
scikit-video              1.1.11                   pypi_0    pypi
scipy                     1.7.1            py39hbe87c03_2
setuptools                58.0.4           py39haa95532_0
six                       1.16.0             pyhd3eb1b0_0
snappy                    1.1.8                h33f27b4_0
sqlite                    3.36.0               h2bbff1b_0
tifffile                  2021.7.2           pyhd3eb1b0_2
tk                        8.6.11               h2bbff1b_0
toolz                     0.11.2             pyhd3eb1b0_0
torchaudio                0.10.0               py39_cu113    pytorch
torchvision               0.11.1               py39_cu113    pytorch
tqdm                      4.62.3                   pypi_0    pypi
typing_extensions         3.10.0.2           pyh06a4308_0
tzdata                    2021e                hda174b7_0
vc                        14.2                 h21ff451_1
vs2015_runtime            14.27.29016          h5e58377_2
wheel                     0.37.0             pyhd3eb1b0_1
wincertstore              0.2              py39haa95532_2
xz                        5.2.5                h62dcd97_0
yaml                      0.2.5                he774522_0
zfp                       0.5.5                hd77b12b_6
zlib                      1.2.11               h62dcd97_4
zstd                      1.4.9                h19a0ad4_0


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
