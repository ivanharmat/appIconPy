# appIconPy
# Python script to easily generate icons for an iOS app

Overall goals of this script:

 * open an image file
 * check if the image is a square and at least 228x228
 * loop through icon dimensions
 * resize image and write to disk
 * add resized image to zip archive
 * remove resized image
 * show success message or error

# Requirements 
 * PIL module for image manipulation - install if you don't have it
```sh
$ sudo pip install image
```

# Usage
```sh
$ python appIconPy.py /path/to/image.png
```

