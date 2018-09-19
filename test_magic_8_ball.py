import unittest

from magic_8_ball import Magic_8_Ball


class Test_Tripple_Check(unittest.TestCase):

    def setUp(self):
        self.magic = Magic_8_Ball()

    def test_returns_the_unique_element(self):
        self.assertIsNotNone(self.magic.main())


if __name__ == "__main__":
    unittest.main()
