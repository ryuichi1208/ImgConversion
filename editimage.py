#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import cv2
import numpy as np
import argparse
import re
from colorama import Fore

# Program Version
VERSION = "1.0.0"

# Select a problem size
M = 10000
K = 1000
N = 5000
total_flops = M*K*(2*N+3)

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


def resize_image(args, src_image_info):
    """
    Image resizing function
    """
    img = cv2.imread(args.input)
    img2 = cv2.resize(img , (int(src_image_info.width*0.1), int(src_image_info.height*0.1)))
    cv2.imwrite(args.o , img2)

    return (0, FileInfo(args.o))


def compress_image(args):
    """
    Image compression processing function
    """
    channel = 1
    src_file_name = args.input
    dst_file_name = args.o

    # Compare extensions
    src_path, src_ext = os.path.splitext(src_file_name)
    dst_path, dst_ext = os.path.splitext(dst_file_name)

    # An error occurs because the extension conversion is not supported
    if not src_ext == dst_ext:
        print("[FAILED] : Invarid extensions", src_ext, dst_ext)
        sys.exit(1)

    img = cv2.imread(src_file_name)

    (result, encimg) = cv2.imencode('.jpg', img, [
        int(cv2.IMWRITE_JPEG_QUALITY),
        int(args.q)
    ])

    if result is False:
        return (1)

    dst = cv2.imdecode(encimg, channel)

    # Image writing process
    cv2.imwrite(dst_file_name, dst)

    return (0, FileInfo(dst_file_name))


def get_args():
    """
    Option parser
    """
    program_name = os.path.basename(__file__) + " : " + VERSION
    parser = argparse.ArgumentParser(description='jpg encoder given images.', prog=program_name)
    parser.add_argument("input", type=str, help='input file')
    parser.add_argument('--version', action='version', version='%(prog)s')
    parser.add_argument('--mode', default='comp', choices=['comp', 'resize'], help='mode choice')
    parser.add_argument("-q", type=str, default='50', help='quality (0 to 100)')
    parser.add_argument("-o", type=str, default='resize.jpg', help='output file (default=resize.jpg)')
    parser.add_argument("--height", type=str, default='100', help='Image height (default=100)')
    parser.add_argument("--witdh", type=str, default='100', help='Image width (default=100)')
    parser.add_argument("--verbose", type=str, default='0', help='debug level')
    args = parser.parse_args()

    if args.verbose:
        global verbose
        verbose = 1

    return args


def print_image_info(src, dst):
    """
    Display original image and converted image information
    """
    print(Fore.GREEN + "[OK] Processing succeeded")

    if verbose:
        print(Fore.GREEN + f'[DEBUG INFO] FILE_NAME : {src.filename} => {dst.filename}')
        print(Fore.GREEN + f'[DEBUG INFO] FILE_SIZE : {src.filesize} => {dst.filesize}')
        print(Fore.GREEN + f'[DEBUG INFO] FILE_WIDTH : {src.width} => {dst.width}')
        print(Fore.GREEN + f'[DEBUG INFO] FILE_HEIGHT : {src.height} => {dst.height}')


def check_file_exit(filepath: str):
    """
    Check if the file exists
    """
    try:
        # Check if file exists
        with open(filepath) as f:
            pass
        # Get information of original image
        return FileInfo(filepath)
    except FileNotFoundError as e:
        return 0
    except AttributeError as e:
        print(Fore.RED + "[FAILED] The specified file is not an image '" + filepath + "'")
        sys.exit(1)
    except IsADirectoryError as e:
        print(Fore.RED + "[FAILED] Specified file is a directory'" + filepath + "'")
        sys.exit(1)


def yes_no_input():
    """
    Select if the destination path already exists
    """
    while True:
        choice = input("Please respond with 'yes' or 'no' [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False


def main():
    args = get_args()

    # Consistency check of input image
    src_image_info = check_file_exit(args.input)
    if src_image_info == 0:
        print(Fore.RED + "[FAILED] There is no such image file '" + args.input + "'")
        sys.exit(1)

    # When the output destination file already exists
    if check_file_exit(args.o):
        if yes_no_input() == False:
            print(Fore.BLUE + "[INFO] : Quit the program...")
            sys.exit(1)

    # Mode select
    if args.mode == 'comp':
        (ret, dst_image_info) = compress_image(args)
    elif args.mode == 'resize':
        (ret, dst_image_info) = resize_image(args, src_image_info)

    # Check end status of conversion process
    if ret != 0:
        print(Fore.RED + "[FAILED] : " + args.mode)
        sys.exit(1)

    # Print result
    print_image_info(src_image_info, dst_image_info)


if __name__ == "__main__":
    main()
