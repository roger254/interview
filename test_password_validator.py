import unittest

from passwordValidator import Password_Validator


class Password_Validator_Test(unittest.TestCase):
    def setUp(self):
        self.validator = Password_Validator()

    def test_return_valid_passowrd(self):
        self.assertEqual("ABd1234@1", self.validator.validate_password("ABd1234@1,a F1#,2w3E*,2We3345"))


if __name__ == "__main__":
    unittest.main()
