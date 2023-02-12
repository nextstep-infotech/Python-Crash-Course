from PIL import Image, ImageFilter

# Option 1: Transpose/Flip
def flip_image(im,option):
    if option == "a":
        out = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    elif option == "b":
        out = im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    elif option == "c":
        out = im.transpose(Image.Transpose.ROTATE_90)
    elif option == "d":
        out = im.transpose(Image.Transpose.ROTATE_180)
    else:
        out = im.transpose(Image.Transpose.ROTATE_270)
    return out

# Option 2: Rotate
def rotate_image(im,angle, expand = False, fillcolor = (0,0,0)):
    out = im.rotate(angle, expand = expand, fillcolor = fillcolor)
    return out

# Option 3: Resize
def resize_image(im, width, height, maintain_aspect_ratio = False):
    size = width,height
    if maintain_aspect_ratio:
        im.thumbnail(size)
        return im
    else:
        out = im.resize(size)
        return out
# Option 4: Scale
def scale_image(im,scale):
    out = im.resize((im.size[0]*scale, im.size[1]*scale))
    return out

# Option 5: Crop
def crop_image(im, box):
    out = im.crop(box)
    return out
# Option 6: Blur
def blur_image(im,blur_value):
    out = im.filter(ImageFilter.BoxBlur(blur_value))
    return out