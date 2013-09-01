# basic math tests for pyANOVA
# time to prove I can do things like add numbers

from __future__ import division # YAY WE'RE IN THE FUTURE

import unittest
import libANOVA

class MathTest(unittest.TestCase):
    
    def setUp(self):
        """Makes a few lists of numbers for doing fun things with"""
        self.ten = [n for n in range(1,11)]
        self.nine = [n for n in range(1,10)]
        self.one_hundred = [n for n in range(1,100)]
    
    def test_even(self):
        self.assertTrue(libANOVA.even(2))
        self.assertTrue(libANOVA.even(4))
        self.assertTrue(libANOVA.even(8))
        self.assertTrue(libANOVA.even(100))
        self.assertTrue(libANOVA.even(12000))
        self.assertTrue(libANOVA.even(42)) # chosen arbitrarily!
        self.assertFalse(libANOVA.even(1))
        self.assertFalse(libANOVA.even(3))
        self.assertFalse(libANOVA.even(5))
        self.assertFalse(libANOVA.even(101))
        self.assertFalse(libANOVA.even(12001))
        self.assertFalse(libANOVA.even(71))
    
    def test_ten_list_product(self):
        self.assertEquals(libANOVA.list_product(self.ten), 3628800)
        
    def test_ten_median(self):
        self.assertEquals(libANOVA.median(self.ten), (11/2))
        
    def test_nine_median(self):
        self.assertEquals(libANOVA.median(self.nine), 5)
        
suite = unittest.TestLoader().loadTestsFromTestCase(MathTest)
unittest.TextTestRunner(verbosity=2).run(suite)