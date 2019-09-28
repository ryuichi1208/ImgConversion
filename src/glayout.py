import cv2
import os
img = cv2.imread("./sample.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("./sample_glay.jpg", gray)

from imgcat import imgcat
imgcat(open("./sample_glay.jpg"))

if __name__ == "__main__":
      PARSER = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=RawTextHelpFormatter)
    PARSER.add_argument("--ip", "-i", required=True,
                        help="OME Appliance IP")
    PARSER.add_argument("--user", "-u", required=True,
                        help="Username for OME Appliance",
                        default="admin")
    PARSER.add_argument("--password", "-p", required=True,
                        help="Password for OME Appliance")
    PARSER.add_argument("--reportid", "-r", required=True,
                        help="a valid report id to execute")
    PARSER.add_argument("--groupid", "-g", required=False,
                        default=0,
                        help="Optional param - Group id to run report against")
    ARGS = PARSER.parse_args()
