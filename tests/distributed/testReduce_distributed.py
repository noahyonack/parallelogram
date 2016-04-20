'''
Ensures correctness for p_reduce() using the PyUnit (unittest) package
'''

import unittest
from parallelogram import parallelogram

class TestReduce_Distributed(unittest.TestCase):

	def test_reduce(self):

		def test1(elt1, elt2):
			return elt1 + elt2

		output = parallelogram.p_reduce(test1, [1,2,3,4,5,6])
		self.assertEqual(output, 21)