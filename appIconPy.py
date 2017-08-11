from PIL import Image
import sys
import os
import zipfile


dimensions = [180, 167, 152, 120, 87, 80, 76, 60, 58, 40, 29, 20]

if len(sys.argv) > 1 : 
	try :
		img = Image.open(sys.argv[1])
		if img.size[0] == img.size[1] : # image is square - icon
			if img.size[0] >= 228 : # image is large enough
				zipFileSavedToFolder = os.path.dirname(os.path.realpath(__file__))
				zipFileName = "appIcons.zip"
				zf = zipfile.ZipFile(zipFileName, mode='w')

				for dimension in range(0, len(dimensions)) :
					filename = str(dimensions[dimension])+"x"+str(dimensions[dimension])+"-"+os.path.basename(sys.argv[1])
					# resize image
					img = img.resize((dimensions[dimension], dimensions[dimension]), Image.ANTIALIAS)
					# save to disk
					img.save(filename)
					# add to zip archive
					zf.write(filename)
					# remove from disk
					os.remove(filename)

				print("Success - the zip file was saved to "+zipFileSavedToFolder+"/"+zipFileName)
				zf.close()
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