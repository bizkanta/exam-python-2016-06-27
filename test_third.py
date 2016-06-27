import unittest
from third import count_letter_in_string

class TestCountLetters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_letter_in_string('', 'a'), (0))

    def test_string_letter_in_it(self):
        self.assertEqual(count_letter_in_string('apple', 'p'), (2))

    def test_string_letter_not_in_it(self):
        self.assertEqual(count_letter_in_string('apple', 'k'), (0))

    def test_string_with_nums(self):
        self.assertEqual(count_letter_in_string('123', '3'), (1))

    def test_int(self):
        self.assertEqual(count_letter_in_string(123, 'a'), (0))

    def test_int_in_int(self):
        self.assertEqual(count_letter_in_string(123, 1), (0))

if __name__ == '__main__':
    unittest.main()
