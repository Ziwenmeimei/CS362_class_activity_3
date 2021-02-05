import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.addition(6,3),9.0)
        self.assertEqual(calculator.addition(1,2),3.0)
        self.assertEqual(calculator.addition(4,8),12.0)
        self.assertEqual(calculator.addition(9,3),12.0)
    def test_substraction(self):
        self.assertEqual(calculator.subtraction(6,3),3.0)
        self.assertEqual(calculator.subtraction(1,2),-1.0)
        self.assertEqual(calculator.subtraction(4,8),-4.0)
        self.assertEqual(calculator.subtraction(9,3),6.0)

    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(6,3),18.0)
        self.assertEqual(calculator.multiplication(1,2),2.0)
        self.assertEqual(calculator.multiplication(4,8),32.0)
        self.assertEqual(calculator.multiplication(9,3),27.0)
    
    def test_division(self):
        self.assertEqual(calculator.division(6,3),2.0)
        self.assertEqual(calculator.division(1,2),0.5)
        self.assertEqual(calculator.division(4,8),0.5)
        self.assertEqual(calculator.division(9,3),3.0)



if __name__ == '__main__':
    unittest.main(verbosity=2)