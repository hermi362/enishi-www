import PIL
import os
import os.path
from PIL import Image

#path = r'C://Users/user/Documents/GONZALEZ/www/img/work_pri_manage39'
#path = r'X://写真/令和２年度/ロイヤル食品工場/6月作業・薬剤散布'
path = r'c://tmp/resize-us'


for file in os.listdir(path):
    f_img = path+"/"+file
    print("resizing " + f_img)
    img = Image.open(f_img)
    exif = img.info['exif']   # get exif_data
    img = img.resize((1280,960))
    img.save(f_img, exif=exif)

    
