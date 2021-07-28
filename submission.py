class Submission:
	def __init__(self, num):
		self.num = num 
		self.picks = 0
		self.score = 0
		self.wins = 0
		self.losses = 0

	def __repr__(self):
		return str(self.num) + ":" + str(self.picks) + ":" + str(round(self.score, 2))