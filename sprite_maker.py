import Image
import glob, sys

def make_sprite(files, width, height, dst_width):
	file_list = glob.glob(files)
	column = dst_width / width
	row = len(file_list) / column
	dst_image = Image.new('RGBA', (dst_width, row * height))
	x = 0
	y = 0
	for infile in file_list:
		src_image = Image.open(infile)
		dst_image.paste(src_image, (x * width, y * height))
		x = x + 1
		if x * width > dst_width:
			x = 0
			y = y + 1
	dst_image.save("sprite.png", "PNG")

if len(sys.argv) < 5:
	print "usage: '*.ext' src_width src_height dst_width"
else:
	make_sprite(str(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
