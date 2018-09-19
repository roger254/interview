import unittest

from additive_sequence import Additive_Seqeuence


class Test_Additive_Sequence(unittest.TestCase):
    def setUp(self):
        self.additive_sequence = Additive_Seqeuence()

    def test_if_returns_true_for_addtive_sequence(self):
        self.assertEqual(True, self.additive_sequence.return_additive_list([6, 6, 12, 18, 30]))


if __name__ == "__main__":
    unittest.main()
