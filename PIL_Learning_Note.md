# [PIL](http://pillow.readthedocs.org/en/latest/handbook/tutorial.html)

### Loading

```
from PIL import Image
im = Image.open("lena.ppm")

```


### Convert to JPEG

```
from __future__ import print_function
import os, sys
from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)
```


#### Create JPEG thumbnails

```
from __future__ import print_function
import os, sys
from PIL import Image

size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for", infile)
```


#### File Identify
When you open a file, the file header is read to determine the file format and extract things like mode, size, and other properties required to decode the file, but the rest of the file is not processed until later.

```
from __future__ import print_function
import sys
from PIL import Image

for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, "%dx%d" % im.size, im.mode)
    except IOError:
        pass
```


#### crop, paste, merge


```
box = (100, 100, 400, 400)
region = im.crop(box)

region = region.transpose(Image.ROTATE_180)
im.paste(region, box)

r, g, b = im.split()
 # The split method creates a set of new images, each containing one band from the original multi-band image.
im = Image.merge("RGB", (b, g, r))
 # The merge function takes a mode and a tuple of images, and combines them into a new image.
```


#### Transforms

```
out = im.resize((128, 128))
out = im.rotate(45) # degrees counter-clockwise

# Converting between modes
im = Image.open("lena.ppm").convert("L")