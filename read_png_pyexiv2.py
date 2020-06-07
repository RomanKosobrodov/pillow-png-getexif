import pyexiv2


fn = "mug_small.png"
image = pyexiv2.Image(fn)
exif = image.read_exif()
print(exif)
