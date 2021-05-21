import unittest
import code

class TestCase(unittest.TestCase):
    def test_code(self):
        self.assertEqual(code.run(2000),"yes")
    #Fail Add
    #def test_false(self):
    #    self.assertEqual(code.run(5),"no")

if __name__ == '__main__':
    unittest.main()
    # coverage report -m leap_year.py
    #pytest -v —cov=leap —cov-report=html
