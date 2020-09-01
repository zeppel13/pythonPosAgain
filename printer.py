import time

from escpos.printer import Usb
from PIL import Image
im = Image.open("seb.jpg")

#Epson = Usb(0x04b8,0x0202)
zj = Usb(0x0416,0x5011)
zj.textln("See chill")
#zj.barcode("12345678", "EAN8")
impls = ["bitImageRaster", "bitImageColumns"]
#for imp in impls:
#    time.sleep(1)
#    zj.image(im, center=True, impl=imp)
long_string = """
Meine Mutter kann deine Mutter nicht kennen. Eureka (eure.ch) Protonmail lolol GPG
Meine Mutter kann deine Mutter nicht kennen. Eureka (eure.ch) Protonmail lolol GPG
Meine Mutter kann deine Mutter nicht kennen. Eureka (eure.ch) Protonmail lolol GPG
Meine Mutter kann deine Mutter nicht kennen. Eureka (eure.ch) Protonmail lolol GPG
Meine Mutter kann deine Mutter nicht kennen. Eureka (eure.ch) Protonmail lolol GPG
Meine Mutter kann deine Mutter nicht kennen. Eureka (eure.ch) Protonmail lolol GPG
Meine Mutter kann deine Mutter nicht kennen. Eureka (eure.ch) Protonmail lolol GPG

"""
#for i in range(1,5):
#    zj.textln("size = {:}".format(i))
#    zj.qr(long_string, size=i)

#zj.soft_barcode("ean8", "13375005", impl="bitImageRaster")