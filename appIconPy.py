from PIL import Image
import sys
import os

basewidth = 100
if len(sys.argv) > 1 :
	try :
		img = Image.open(sys.argv[1])
		if img.size[0] == img.size[1] :
			if img.size[0] >= 228 :
				filename = "resized-"+os.path.basename(sys.argv[1])
				wpercent = (basewidth / float(img.size[0]))
				hsize = int((float(img.size[1]) * float(wpercent)))
				img = img.resize((basewidth, hsize), Image.ANTIALIAS)
				img.save(filename)
			else :
				print("Image is too small - minimum 228x228 needed")
		else :
			print("This image is not a square image, can't generate icon")
	except FileNotFoundError as e:
		print("File not found - "+sys.argv[1])
	except OSError :
		print("The file is not an image")
else :
	print("Error - Enter file name")