#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import cv2
import time
import datetime
import numpy as np
import re
from colorama import Fore

from src.dispatch import *
from src.logger import logger

# Select a problem size
M = 10000
K = 1000
N = 5000
total_flops = M*K*(2*N+3)

# For filesize calculation
KB = 1024.0
MB = 1024.0 ** 2
GB = 1024.0 ** 3
TB = 1024.0 ** 4
PT = 1024.0 ** 5

# Debug Level
verbose = 0


class FileInfo():
    """
    Class for holding file information
    """
    def __init__(self, filename):
        img = cv2.imread(filename, cv2.IMREAD_COLOR)
        img_height, img_width, channels = img.shape[:3]
        self.__filename = filename
        self.__filesize = os.path.getsize(filename)
        self.__ctime = os.stat(filename).st_mtime
        self.__height = img_height
        self.__width = img_width

    @property
    def filename(self):
        return self.__filename

    @property
    def filesize(self):
        return self.__filesize

    @property
    def ctime(self):
        return self.__ctime

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @filename.setter
    def filename(self, filename):
        self.__filename = filename


def main():
    """
    ImgConversion main function
    """
    args = get_option_and_parse()
    dispatch_exec_mode(args)


if __name__ == "__main__":
    logger("INFO", "START")
    main()
    logger("INFO", "END")
