class Submission:
	def __init__(self, num):
		self.num = num 
		self.picks = 0

	def __repr__(self):
		return str(self.num) + ":" + str(self.picks)