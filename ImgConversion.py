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
