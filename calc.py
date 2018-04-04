# Making a working calculator

class Calc(object):
	"""docstring for Calc"""
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def add(self):
		return self.num1 + self.num2

	def multi(self):
		return self.num1 * self.num2

	def subtr(self):
		return self.num1 - self.num2

	def div(self):
		if self.num2 == 0:
			raise ValueError("Cannot perform the division")
		else:
			return self.num1/self.num2