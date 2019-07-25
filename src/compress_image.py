import os
import sys
import cv2
import subprocess

def compare_ext(src_ext, dst_ext):
    """
    An error occurs because the extension conversion is not supported
    """
    if not src_ext == dst_ext:
        return 1
    return 0

def open_image(dst_file_name):
    cmd = ["open", dst_file_name]
    res = subprocess.call(cmd)


def compress_image(args):
    """
    Image compression processing function
    """
    channel = 1
    src_file_name = args.input
    dst_file_name = args.output

    # Compare extensions
    src_path, src_ext = os.path.splitext(src_file_name)
    dst_path, dst_ext = os.path.splitext(dst_file_name)

    if compare_ext(src_ext, dst_ext):
        print("[FAILED] : Invarid extensions", src_ext, dst_ext)
        sys.exit(1)

    img = cv2.imread(src_file_name)

    (result, encimg) = cv2.imencode('.jpg', img, [
        int(cv2.IMWRITE_JPEG_QUALITY),
        int(args.quality)
    ])

    if result is False:
        return (1)

    dst = cv2.imdecode(encimg, channel)

    # Image writing process
    cv2.imwrite(dst_file_name, dst)

    if args.open:
        open_image(dst_file_name)

