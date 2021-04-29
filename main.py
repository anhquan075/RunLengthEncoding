import argparse
from PIL import Image
import utils
from Detail import Detail
import os

def encodeImage(path):
	img1 = Image.open(path)
	orgimg = list(img1.getdata(0))
	encodedimg = utils.encodeImage(orgimg, img1.size[0], img1.size[1], img1.mode)
	tempimg = Detail(encodedimg, 1, img1.size[0], img1.size[1], img1.mode, img1.getpalette())
	compsize, filepath = utils.saveCompressedToFile(tempimg, path)
	print("Encoded file saved to: " + filepath)
	print("The Compression Ratio: {} %".format(round((compsize / os.stat(path).st_size) * 100, 2)))

def decodeImage(path):
	compimg = utils.openFileToCompressed(path)
	decodedimg = utils.decodeImage(compimg.compressed, compimg.width, compimg.height, compimg.mode)
	newimage = Image.new(compimg.mode, (compimg.width, compimg.height))
	newimage.putdata(decodedimg)
	if compimg.mode == 'P':
		newimage.putpalette(compimg.palette)
	newfilepath = path[:len(path) - 9] + "-copy.bmp"
	newimage.save(newfilepath)
	print("Decoded file saved to: " + newfilepath)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-e', '--encode', help = 'Image to encode.')
	parser.add_argument('-d', '--decode', help = 'Compressed file to decode.')

	args = parser.parse_args()

	if not (args.encode or args.decode):
		parser.error('No action requested, add -e or -d')

	args = vars(args)

	if args['encode'] is not None:
		encodeImage(args['encode'])
	elif args['decode'] is not None:
		decodeImage(args['decode'])
	else:
		print('Enter arguments correctly')
