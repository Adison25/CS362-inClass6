import unittest
import leap

class TestCase(unittest.TestCase):
    def test_true(self):
        self.assertEqual(leap.run(2000),"yes")
    #Fail Add
    def test_false(self):
        self.assertEqual(leap.run(5),"no")

if __name__ == '__main__':
    unittest.main()