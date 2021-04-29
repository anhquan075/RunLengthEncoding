'''
Nguyen Le Anh Quan - 19522081
Tham khao tu source: https://github.com/ormanli/run-length-encoding

'''

import unittest
from PIL import Image
import os
from Detail import Detail
import glob
from timer import timewith
import pprint
import math
import utils
import json

class Test(unittest.TestCase):

	results = {}

	def addNameToDictionary(self, depth, image, result, value):
		if depth not in self.results:
			self.results[depth] = {}
		if image not in self.results[depth]:
			self.results[depth][image] = {}
		if result not in self.results[depth][image]:
			self.results[depth][image][result] = {}
		self.results[depth][image][result] = value

	def testBW(self):
		imgdirname = "./images/black&white"

		filelist = glob.glob(imgdirname + "/*.bmp")
		for file in filelist:
			img1 = Image.open(file)

			orgimg = list(img1.getdata(0))

			with timewith('Black&White') as timer:
				encodedimg = utils.encodeImage(orgimg, img1.size[0], img1.size[1], img1.mode)
				self.addNameToDictionary('BW', file, 'Encode', timer.checkpoint('Encode Image: ' + file))

				tempimg = Detail(encodedimg, 1, img1.size[0], img1.size[1], img1.mode)
				compsize, filepath = utils.saveCompressedToFile(tempimg, file)
				statinfo = os.stat(file)
				compimg = utils.openFileToCompressed(file + ".comp")
				self.addNameToDictionary('BW', file, 'Compression Ratio', math.ceil((compsize / statinfo.st_size) * 1000) / 1000)
				timer.checkpoint('Compression Ratio: ' + file)

				decodedimg = utils.decodeImage(compimg.compressed, compimg.width, compimg.height, compimg.mode)
				self.addNameToDictionary('BW', file, 'Decode', timer.checkpoint('Decode Image: ' + file))
				self.addNameToDictionary('BW', file, 'Equality', str(orgimg == decodedimg))

	def testGRY4BIT(self):
		imgdirname = "./images/4bit"

		filelist = glob.glob(imgdirname + "/*.bmp")
		for file in filelist:
			img1 = Image.open(file)

			orgimg = list(img1.getdata(0))
			print(file)
			with timewith('4bit Number') as timer:
				encodedimg = utils.encodeImage(orgimg, img1.size[0], img1.size[1], img1.mode)
				self.addNameToDictionary('4bit', file, 'Encode', timer.checkpoint('Encode Image Mode '  + " " + file))
				tempimg = Detail(encodedimg, 1, img1.size[0], img1.size[1], img1.mode, img1.getpalette())
				compsize, filepath = utils.saveCompressedToFile(tempimg, file)
				statinfo = os.stat(file)
				compimg = utils.openFileToCompressed(file + ".comp")
				self.addNameToDictionary('4bit', file, 'Compression Ratio', math.ceil((compsize / statinfo.st_size) * 1000) / 1000)
				timer.checkpoint('Compression Ratio:' + file)

				decodedimg = utils.decodeImage(compimg.compressed, compimg.width, compimg.height, compimg.mode)
				self.addNameToDictionary('4bit', file, 'Decode', timer.checkpoint('Decode Image Mode '  + " " + file))
				self.addNameToDictionary('4bit', file, 'Equality', str(orgimg == decodedimg))

	def testGRY8BIT(self):
		imgdirname = "./images/8bit"

		filelist = glob.glob(imgdirname + "/*.bmp")
		for file in filelist:
			img1 = Image.open(file)

			orgimg = list(img1.getdata(0))

			with timewith('8bit Number ' ) as timer:
				encodedimg = utils.encodeImage(orgimg, img1.size[0], img1.size[1], img1.mode)
				self.addNameToDictionary('8bit', file, 'Encode', timer.checkpoint('Encode Image Mode '  + " " + file))

				tempimg = Detail(encodedimg, 1, img1.size[0], img1.size[1], img1.mode)
				compsize, filepath = utils.saveCompressedToFile(tempimg, file)
				statinfo = os.stat(file)
				compimg = utils.openFileToCompressed(file + ".comp")
				self.addNameToDictionary('8bit', file, 'Compression Ratio', math.ceil((compsize / statinfo.st_size) * 1000) / 1000)
				timer.checkpoint('Compression Ratio '  + " " + file)

				decodedimg = utils.decodeImage(compimg.compressed, compimg.width, compimg.height, compimg.mode)
				self.addNameToDictionary('8bit', file, 'Decode', timer.checkpoint('Decode Image Mode '  + " " + file))
				self.addNameToDictionary('8bit', file, 'Equality', str(orgimg == decodedimg))

	def testResult(self):
		pprint.pprint(self.results)
		with open('results.json' , 'w') as f:
			json.dump(self.results, f)
		

if __name__ == "__main__":
# 	import sys;sys.argv = ['', 'Test.testEncode']
	unittest.main()
