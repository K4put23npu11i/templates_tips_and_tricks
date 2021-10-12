import unittest
import calc


class TestCalc(unittest.TestCase):

    # methods hast to start with test_
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
        result = calc.add(-1, 1)
        self.assertEqual(result, 0)
        result = calc.add(-1, -1)
        self.assertEqual(result, -2)

    def test_subtract(self):
        result = calc.subtract(10, 5)
        self.assertEqual(result, 5)
        result = calc.subtract(-1, 1)
        self.assertEqual(result, -2)
        result = calc.subtract(-1, -1)
        self.assertEqual(result, 0)

    def test_multiply(self):
        result = calc.multiply(10, 5)
        self.assertEqual(result, 50)
        result = calc.multiply(-1, 1)
        self.assertEqual(result, -1)
        result = calc.multiply(-2, -2)
        self.assertEqual(result, 4)

    def test_divide(self):
        result = calc.divide(10, 5)
        self.assertEqual(result, 2)
        result = calc.divide(-1, 1)
        self.assertEqual(result, -1)
        result = calc.divide(-1, -1)
        self.assertEqual(result, 1)

        self.assertRaises(ValueError, calc.divide, 10, 0)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
