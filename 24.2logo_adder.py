
from PIL import Image
import os

# Load logo file
logo_path = r"E:\For YT Videos\Courses\Python Crash Course\Nepali\24 Image Manipulation Project\Project 2\Tutorial\firebird.png"
logo = Image.open(logo_path)
# print(logo.size)
# logo.show()

image_path = r"E:\For YT Videos\Courses\Python Crash Course\Nepali\24 Image Manipulation Project\Project 2\Tutorial\WallpaperPC"

os.chdir(image_path)

for i, img in enumerate(os.listdir(),1):

    image = Image.open(img)
    basewidth = int(image.size[0]/10)
    wpercent = basewidth/logo.size[0]
    hsize = int(logo.size[1]*wpercent)
    logo = logo.resize((basewidth,hsize))

    ext = img.split(".")[-1]
    valid_ext = ["jpg", "png", "svg", "jpeg", "gif"]
    if ext.lower() in valid_ext:
        #Add logo to image
        position = (image.size[0]-logo.size[0], 0)
        image.paste(logo, position)
        image.save(r"E:\For YT Videos\Courses\Python Crash Course\Nepali\24 Image Manipulation Project\Project 2\Tutorial\WallpaperPCwithLogo"+f"\Final_image{i}.{ext}")



