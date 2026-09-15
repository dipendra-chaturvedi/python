import unittest
from salary import calculate_salary


class TestSalary(unittest.TestCase):

    def test_calculate_salary(self):
        result = calculate_salary(60000, 10000)
        self.assertEqual(result, 70000)


if __name__ == "__main__":
    unittest.main()