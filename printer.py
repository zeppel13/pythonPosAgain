#
import time
import sys
from escpos.printer import Usb
from PIL import Image
# file printer

zj = Usb(0x0416, 0x5011)
zj.textln("See chill")


def printThis(val):
    im = Image.open(val)
    time.sleep(0.4)
    zj.image(im, impl="bitImageRaster")


for val in sys.argv[1:]:
    print(val)
    printThis(val)


