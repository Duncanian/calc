from calc import Calc
import unittest

class TestCalc(unittest.TestCase):
	"""docstring for TestCalc"""
	def test_add(self):
		comb1 = Calc(4, 2)
		sum1 = comb1.add()
		self.assertEqual(sum1, 6)

	def test_multi(self):
		comb1 = Calc(4, 2)
		mul1 = comb1.multi()
		self.assertEqual(mul1, 8)

	def test_subtr(self):
		comb1 = Calc(4, 2)
		subtr1 = comb1.subtr()
		self.assertEqual(subtr1, 2)

	def test_div(self):
		comb1 = Calc(4, 2)
		comb2 = Calc(4, 0)
		div = comb1.div()
		self.assertEqual(div, 2)

		with self.assertRaises(ValueError):
			comb2.div()


if __name__ == "__main__":
	unittest.main()