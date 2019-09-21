
![GitHub release (latest by date)](https://img.shields.io/github/v/release/ryuichi1208/ImgConversion)
![GitHub repo size](https://img.shields.io/github/repo-size/ryuichi1208/ImgConversion)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ryuichi1208/ImgConversion)
![Python version](https://img.shields.io/badge/Python-3.6%2F3.7-red)

## Project Title

ImgConversion

## Description


"ImageConversion" is a tool to compress / resize / change the image.

## Features

* Image compression
* Image resize
* Extension change

## Requirement

* Python 3.6+
* cv2
* numpy
* argparse
* colorama

## Usage

```
usage: editimage.py : 1.0.0 [-h] [--version] [--mode {comp,resize}] [-q Q]
                            [-o O] [--height HEIGHT] [--witdh WITDH]
                            input
jpg encoder given images.
positional arguments:
  input                 input file
optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --mode {comp,resize}  mode choice
  -q Q                  quality (0 to 100)
  -o O                  output file (default=resize.jpg)
  --height HEIGHT       Image height (default=100)
  --witdh WITDH         Image width (default=100)
```

## Installation

```
git clone https://github.com/ryuichi1208/imgconversion.git
```

## License

Open Source: Apache License 2.0

## Authors

* [ryuichi1208](https://github.com/ryuichi1208)
