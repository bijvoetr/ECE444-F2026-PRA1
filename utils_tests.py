import unittest
from utils import reversed, formatter


class TestUtils(unittest.TestCase):

    def test_reversed(self):
        self.assertEqual(reversed(1234), 4321)
        self.assertEqual(reversed("1234"), 4321)
        self.assertEqual(reversed(1234.0), 4321)

    def test_formatter(self):
        self.assertEqual(formatter(10), ("1010", "12"))
        self.assertEqual(formatter("10"), ("1010", "12"))
        self.assertEqual(formatter(10.0), ("1010", "12"))


if __name__ == "__main__":
    unittest.main()