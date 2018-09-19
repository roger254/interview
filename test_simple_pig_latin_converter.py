import unittest

from Simple_Pig_Latin_Converter import Simple_Pig_Latin_Converter


class Test_Simple_Latin_Pig_Converter(unittest.TestCase):

    def setUp(self):
        self.converter = Simple_Pig_Latin_Converter()

    def test_returns_valid_convertion(self):
        self.assertEqual(True, self.converter.pig_latin_converter("arrb6???4xxbl5???eee5"))
        self.assertEqual(True, self.converter.pig_latin_converter("acc?7??sss?3rr1??????5"))
        self.assertEqual(False, self.converter.pig_latin_converter("5??aaaaaaaaaaaaaaaaaaa?5?5"))
        self.assertEqual(True, self.converter.pig_latin_converter("9???1???9???1???9"))
        self.assertEqual(False, self.converter.pig_latin_converter("aa6?9"))


if __name__ == "__main__":
    unittest.main()
