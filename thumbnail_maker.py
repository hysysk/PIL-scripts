import Image
import os, sys, glob
if len(sys.argv) < 3:
	sys.exit("usage: '*.ext' size quality")

fileList = glob.glob(sys.argv[1])
for infile in fileList:
	file,ext = os.path.splitext(infile)
	outfile = file + "_thumb" + ext
	img = Image.open(infile)
	img.thumbnail((int(sys.argv[2]),'auto'), Image.ANTIALIAS)
	outExt = ""
	if ext == "jpg":
		outExt = "JPEG"
		quality = int(sys.argv[3])
	elif ext == "gif":
		outExt = "GIF"
	elif ext == "png":
		outExt = "PNG"
		
	img.save(outfile, outExt, quality=95)
