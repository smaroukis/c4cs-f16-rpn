import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calcualte("3 5 -")
		self.assertEqual(2, result)
	def test_badstring(self):
		with self.assertRaises(TypeError):
			rpn.calcuate("1 2 3 +")
	def test_multiply(self):
		result = rpn.calculate("2 3 *")
		self.assertEqual(6, result)
	def test_divide(self):
		result = rpn.calculate("10 5 /")
		self.assertEqual(2, result)
	
