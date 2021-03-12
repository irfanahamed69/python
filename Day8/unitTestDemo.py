import unittest
from isupper import check_is_upper

class Testing(unittest.TestCase):
    def test_boolean_is_upper(self):
        self.assertEqual(check_is_upper('HELLO'),True)

    def test_boolean_is_notUpper(self):
        self.assertEqual(check_is_upper('hello'),True)

if __name__ == '__main__':
    unittest.main()

#run the file as py unitTestDemo.py -v
