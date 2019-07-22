import os
import cv2

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

    if compare_ext(src_ext, dst_ext):
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
