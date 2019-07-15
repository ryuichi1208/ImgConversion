#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import cv2
import numpy as np
import argparse

version = "1.0.0"

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
    img = cv2.imread(args.input)

    (result, encimg) = cv2.imencode('.jpg', img, [
        int(cv2.IMWRITE_JPEG_QUALITY),
        int(args.q)
    ])

    if result == False:
        return (1)

    dst = cv2.imdecode(encimg, channel)
    cv2.imwrite(args.o, dst)

    return (0, FileInfo(args.o))

def get_args():
    """
    Option parser
    """
    program_name = os.path.basename(__file__) + " : " + version
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

def main():
    args = get_args()

    src = FileInfo(args.input)

    if args.mode == 'comp':
        (ret, dst) = compress_image(args)
    elif args.mode == 'resize':
        ret = resize_image(args)

    if ret != 0:
        print("[FAILED] : " + args.mode)

    print(f'{src.filename} to {dst.filename}')
    print(f'{src.filesize} to {dst.filesize}')

if __name__ == "__main__" :
    main()
