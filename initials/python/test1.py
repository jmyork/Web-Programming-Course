import unittest
from prime import is_prime

class Tests(unittest.TestCase):
    def test_1(self):
        """ this part tests if the number 1 is  prime"""
        self.assertFalse(is_prime(1))
        
    def test_2(self):
         """ this part tests if the number 2 is  prime"""
         self.assertTrue(is_prime(2))
         
    def test_3(self):
         """ this part tests if the number 3 is  prime"""
         self.assertTrue(is_prime(3))
         
    def test_4(self):
         """ this part tests if the number 4 is  prime"""
         self.assertFalse(is_prime(4))
         
    def test_5(self):
         """ this part tests if the number 5 is  prime"""
         self.assertTrue(is_prime(5))
         
    def test_6(self):
         """ this part tests if the number 6 is  prime"""
         self.assertFalse(is_prime(6))
         
    def test_7(self):
         """ this part tests if the number 7 is  prime"""
         self.assertTrue(is_prime(7))
         
    def test_8(self):
         """ this part tests if the number 8 is  prime"""
         self.assertFalse(is_prime(8))
    def test_9(self):
         """This part treat a  generic case"""
         self.assertTrue(is_prime(111212))
         
               
if __name__== "__main__":
     unittest.main()