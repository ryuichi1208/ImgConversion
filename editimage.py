#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import cv2
import time
import numpy as np
import argparse
import re
from colorama import Fore

import argparse
import os
import pandas as pd
import yaml
from tqdm import tqdm


from utils.db_connection import get_connection
from utils.create_dir import create_dir
from utils.logger import get_logger
from utils.read_file import read_file


logging = get_logger()


def download_dataset(sql_file, conn, output_file):
    sql = read_file(sql_file)
    logging.info(sql)

    df = pd.read_sql_query(sql, con=conn, chunksize=100000)
    chunk = next(df)
    chunk.drop_duplicates().to_csv(output_file, mode='w', index=None)
    for chunk in tqdm(df):
        chunk.drop_duplicates().to_csv(output_file, mode='a', index=None, header=None)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--config_file', type=str, default='./etc/foo.cfg')

    args = parser.parse_args()
    logging.info("Args : {}".format(args))

    config = yaml.safe_load(open(args.config_file))
    sql_file = config['sql_file']
    output_file = config['output_file']

    create_dir(os.path.dirname(output_file))

    if os.path.exists(output_file):
        logging.warning('There is already a file with name %s' % output_file)
    else:
        logging.info('Downloading download_dataset from database')
        download_dataset(sql_file, get_connection(config['db']), output_file)
    logging.info("End of file.")

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


def resize_image(args, src_image_info):
    """
    Image resizing function
    """
    src_file_name = args.input
    dst_file_name = args.o

    img = cv2.imread(src_file_name)
    img2 = cv2.resize(img, (int(src_image_info.width * float(args.width)), int(src_image_info.height * float(args.height))))
    cv2.imwrite(dst_file_name, img2)

    return (0, FileInfo(dst_file_name))


def roundstr(size):
    """
<<<<<<< HEAD
    Perform round-up processing
=======
    Round up and return as string
>>>>>>> 30cbdc2cc2d984b27aea19058fce1d9b83c70dc2
    """
    return str(round(size, 1))


def filesize(bytesize):
    """
    Format file size
    """
    if bytesize < 1024:
        return str(bytesize) + ' B'
    elif bytesize < 1024 ** 2:
        return roundstr(bytesize / 1024.0) + ' KB'
    elif bytesize < 1024 ** 3:
        return roundstr(bytesize / (1024.0 ** 2)) + ' MB'
    elif bytesize < 1024 ** 4:
        return roundstr(bytesize / (1024.0 ** 3)) + ' GB'
    elif bytesize < 1024 ** 5:
        return roundstr(bytesize / (1024.0 ** 4)) + ' TB'
    else:
        return str(bytesize) + ' B'

def compare_ext(src_ext, dst_ext):
    """
    An error occurs because the extension conversion is not supported
    """
    if not src_ext == dst_ext:
        return 1
    return 0


def is_check_ext(src_ext, dst_ext):
    """
    An error occurs because the extension conversion is not supported
    """
    if not src_ext == dst_ext:
        return 1
    else:
        return 0


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

<<<<<<< HEAD
    if is_check_ext(src_ext, dst_ext):
=======
    if compare_ext(src_ext, dst_ext):
>>>>>>> 30cbdc2cc2d984b27aea19058fce1d9b83c70dc2
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


"""
img = cv2.imread('green_red_apple.png')
transpose_img = img.transpose(1,0,2)
clockwise = transpose_img[:,::-1]
counter_clockwise = transpose_img[::-1]
"""

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
    parser.add_argument("--height", type=str, default='1', help='Image height 0.1 to 1.0 (default1.0)')
    parser.add_argument("--width", type=str, default='1', help='Image width 0.1 to 1.0 (default=1.0)')
    parser.add_argument("--verbose", type=str, default='0', help='debug level')
    args = parser.parse_args()

    if int(args.verbose) > 0:
        global verbose
        verbose = 1

    return args


def print_image_info(src, dst):
    """
    Display original image and converted image information
    """
    if verbose:
        from tqdm import tqdm
        for _ in tqdm(range(100), ncols=80):
            time.sleep(0.01)
        print(Fore.GREEN + f'[DEBUG INFO] FILE_NAME   : {src.filename} => {dst.filename}')
        print(Fore.GREEN + f'[DEBUG INFO] FILE_SIZE   : {filesize(int(src.filesize))} => {filesize(int(dst.filesize))}')
        print(Fore.GREEN + f'[DEBUG INFO] FILE_WIDTH  : {src.width} => {dst.width}')
        print(Fore.GREEN + f'[DEBUG INFO] FILE_HEIGHT : {src.height} => {dst.height}')

    print(Fore.GREEN + "[OK] Processing succeeded")


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
        # Dig and check directories
        if check_file_exit(filepath + '/resize.jpg') != 0:
            print(Fore.RED + "[FAILED] Specified file is a directory'" + filepath + "'")
            sys.exit(1)


def image_oveimage_overwrite_select():
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
        if image_oveimage_overwrite_select() is False:
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
