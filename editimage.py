#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import cv2
import numpy as np
import argparse
import re

# Program Version
VERSION = "1.0.0"

# Select a problem size
M = 10000
K = 1000
N = 5000
total_flops = M*K*(2*N+3)

class FileInfo():
    """
    Class for holding file information
    """
    def __init__(self, filename):
        self.__filename = filename
        self.__filesize = os.path.getsize(filename)
        self.__ctime    = os.stat(filename).st_mtime

    @property
    def filename(self):
        return self.__filename

    @property
    def filesize(self):
        return self.__filesize

    @property
    def ctime(self):
        return self.__ctime

def resize_image(args):
    """
    Image resizing function
    """
    print("h", args.height)
    print("w", args.witdh)

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
    if src_ext != dst_ext:
        print("[FAILED] : Invarid extensions", src_ext, dst_ext)
        sys.exit(1)

    img = cv2.imread(src_file_name)

    (result, encimg) = cv2.imencode('.jpg', img, [
        int(cv2.IMWRITE_JPEG_QUALITY),
        int(args.q)
    ])

    if result == False:
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
    args = parser.parse_args()

    return args

def print_image_info(src, dst):
    """
    Display original image and converted image information
    """
    print(Fore.WHITE + f'{src.filename} to {dst.filename}')
    print(Fore.WHITE + f'{src.filesize} to {dst.filesize}')

def main():
    print_usage()
    args = get_args()

    # Get information of original image
    src_image_info = FileInfo(args.input)

    if args.mode == 'comp':
        (ret, dst_image_info) = compress_image(args)
    elif args.mode == 'resize':
        ret = resize_image(args)

    # Check end status of conversion process
    if ret != 0:
        print("[FAILED] : " + args.mode)
        sys.exit(1)

    print_image_info(src_image_info, dst_image_info)

if __name__ == "__main__" :
    main()
