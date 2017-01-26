import unittest
import fb 

class TestFizzBuzz(unittest.TestCase):


	def test_Fizz(self):
		self.assertEqual("Fizz", fb.fizzBuzz(3))

	def test_nr(self):
		self.assertEqual(4, fb.fizzBuzz(4))

	def test_Buzz(self):
		self.assertEqual("Buzz", fb.fizzBuzz(5))

	def test_FizzBuzz(self):
		self.assertEqual("FizzBuzz", fb.fizzBuzz(15))

if __name__ == '__main__':
	unittest.main()
