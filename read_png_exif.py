import sys
from PIL import Image, __version__

print(f"PIL version {__version__}")
print(f"Python version {sys.version}")
fn = "mug_small.png"
img = Image.open(fn)
exif = img.getexif()
print(exif)
