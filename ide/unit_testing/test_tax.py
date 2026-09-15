import unittest
from tax import calculate_tax


class TestTax(unittest.TestCase):

    def test_tax_above_limit(self):
        result = calculate_tax(60000)
        self.assertEqual(result, 6000)


if __name__ == "__main__":
    unittest.main()