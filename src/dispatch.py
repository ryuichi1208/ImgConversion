import os
import platform
import argparse
from src.compress_image import *
from src.logger import logger

# Program Version
VERSION = "1.0.0"


def get_option_and_parse():
    """
    Option parser
    """
    # Top Level
    program_name = os.path.basename(__file__) + " : " + VERSION
    parser = argparse.ArgumentParser(description='jpg encoder given images.', prog=program_name)
    subparsers = parser.add_subparsers()

    # comp
    parser_comp = subparsers.add_parser('comp', help='see `comp -h`')
    parser_comp.add_argument("input", type=str, help='Input file')
    parser_comp.add_argument('-o', '--output', default='resize.jpg', help='Output file')
    parser_comp.add_argument('-q', '--quality', type=int, default=50, help='quality (0 to 100)')
    parser_comp.add_argument("--verbose", type=int, default='0', help='debug level')
    if platform.system() == "Darwin":
        parser_comp.add_argument('--open', action='store_true', help='Open resized image')

    # resize
    parser_resize = subparsers.add_parser('resize', help='see `resize -h`')
    parser_resize.add_argument('-i', '--input', help='Imput file')
    parser_resize.add_argument('-t', '--height', type=int, default=1, help='height (0.1 to 1.0)')
    parser_resize.add_argument('-w', '--width', type=int, default=1, help='width (0.1 to 1.0)')
    parser_resize.add_argument("--verbose", type=int, default='0', help='debug level')

    # rename
    parser_resize = subparsers.add_parser('rename', help='see `resize -h`')

    args = parser.parse_args()

    if hasattr(args, 'verbose') and args.verbose > 0:
        global verbose
        verbose = 1
        print("[DEBUG INFO] : VERBOSE MODE ON")

    return args


def dispatch_exec_mode(args):
    """
    Dispatch to a function in the mode selected by the argument
    """
    if hasattr(args, 'quality'):
        if args.quality < 0 or 100 < args.quality:
            logger("ERROR", "Invalid argument of quality value", 1)
        compress_image(args)
    elif hasattr(args, 'height'):
        print("MODE resize")
    else:
        logger("ERROR", "Unkown Exec Mode", 1)
