import PIL
import os
import os.path
from PIL import Image

def visitDir(path):
    # list all files and dirs in path
    for f in os.listdir(path):
        pf = os.path.join(path, f)
        if os.path.isdir(pf):
            print("-- Entering directory %s" % pf)
            visitDir(pf)
        else:
            if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg'):
                shrinkJPEG(pf)

def shrinkJPEG(f_img):
    print("   Resizing %s ..." % f_img)
    # TODO: find a way to ignore .jpg files that do not contain JPEG data (e.g. corrupted files)

    img = Image.open(fp=f_img, formats=['JPEG'])
    if img.width <= 1280:
        print("** NOT OVER 1280 PIXELS WIDE, IGNORING: %s" % f_img)
        return

    exif = b''  # init with an empty bytearray
    if 'exif' in img.info:
        exif = img.info['exif']   # get exif_data
    img = img.resize((1280,960))
    img.save(f_img, exif=exif)
    # NOTE: saving EXIF data like this means that the new reduced resolution is NOT in the EXIF data.


#path = r'C://Users/user/Documents/GONZALEZ/www/img/work_pri_manage39'
#path = r'X://写真/令和２年度/ロイヤル食品工場/6月作業・薬剤散布'

for path in [r'c:\tmp\resize-us']:

    # for file in os.listdir(path):
    visitDir(path)



