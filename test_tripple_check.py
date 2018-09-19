import unittest

from tripple_check import Tripple_Check


class Test_Tripple_Check(unittest.TestCase):

    def setUp(self):
        self.checker = Tripple_Check()

    def test_returns_the_unique_element(self):
        self.assertEqual(4, self.checker.return_unique_element([5, 3, 4, 3, 5, 5, 3]))


if __name__ == "__main__":
    unittest.main()
