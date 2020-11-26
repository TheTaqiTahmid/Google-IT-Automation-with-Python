# Write a simple unit test for our rearrange name function 
# Remember the name of the function will have to start with test 

from UPTIOS_week5 import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    
    def test_rearrange(self):
        testcase = 'Lovelace, Ada'
        expected = 'Ada Lovelace'
        result = rearrange_name(testcase)
        self.assertEqual(result, expected, 'Should be Ada Lovelace')

    def test_empty(self):
        testcase = ''
        # expected = ''
        result = rearrange_name(testcase)
        self.assertIs(result, '', 'Should be empty string')
    
    def test_unexpected_char(self):
        testcase = 'Tadf21@, gdh3'
        expected = ''
        result = rearrange_name(testcase)
        self.assertEqual(result, expected)

    def test_double_name(self):
        testcase = 'Hopper, Grace M.'
        expected = 'Grace M. Hopper'
        result = rearrange_name(testcase)
        self.assertEqual(result, expected, 'Should be Grace M. Hopper')

    def test_one_name(self):
        testcase = 'Taqi'
        expected = 'Taqi'
        result = rearrange_name(testcase)
        self.assertEqual(result, expected, 'Should be Taqi')

if __name__ == '__main__':
    unittest.main()
