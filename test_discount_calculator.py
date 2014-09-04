import unittest

from discount_calculator import discount_calc

class DiscountCalculatorTests(unittest.TestCase):
	def testRelativeDiscountApplication(self):
		# Ensures that relative discounts get applied to the total item cost not the item cost after other discounts
		cost = discount_calc(100, 10, 10)
		self.assertEqual(cost, 80)

	def testNegativeRelativeDiscounts(self):
		with self.assertRaises(ValueError):
			cost = discount_calc(100, -10, 0)


if __name__ == "__main__":
	unittest.main()
