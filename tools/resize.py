import PIL
import os
import os.path
from PIL import Image

#path = r'C://Users/user/Documents/GONZALEZ/www/img/work_pri_manage39'
#path = r'X://写真/令和２年度/ロイヤル食品工場/6月作業・薬剤散布'
path = r'C://Users/PC08/Documents/www/img/work_gov_manage57'



size = (1280, 1280)

for file in os.listdir(path):
    infile = path+"/"+file
    outfile = os.path.splitext(infile)[0] + ".thumb.jpg"
    if infile != outfile:
      try:
        print("resizing " + outfile)
        with Image.open(infile) as img:
          img.thumbnail(size)
          img.save(outfile, "JPEG")
      except OSError:
        print("cannot resize " + outfile)

