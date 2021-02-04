import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.addition(6,3),9.0)

    def test_substraction(self):
        self.assertEqual(calculator.subtraction(6,3),3.0)

    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(6,3),18.0)
    
    def test_division(self):
        self.assertEqual(calculator.division(6,3),2.0)



if __name__ == '__main__':
    unittest.main()