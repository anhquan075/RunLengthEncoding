class Detail:
	def __init__(self, compressed, hist, width, height, mode , palette = None):
		'''
		Constructor
		'''
		self.compressed = compressed
		self.hist = hist
		self.height = height
		self.width = width
		self.mode = mode
		self.palette = palette
