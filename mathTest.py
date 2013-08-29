# basic math tests for pyANOVA

import unittest
import libANOVA

class MathTest(unittest.TestCase):
    
    def setUp(self):
        self.ten = [n for n in range(10)]
        self.nine = [n for n in range(9)]
        self.one_hundred = [n for n in range(100)]
    
    def test_ten_list_produc(self):
        self.assertEquals(libANOVA.list_product(self.ten), 3628800)
        
    def test_ten_median(self):
        self.assertEquals(libANOVA.median(self.ten), (11/2))
        
    def test_nine_median(self):
        self.assertEquals(libANOVA.median(self.ten), 5)
        
suite = unittest.TestLoader().loadTestsFromTestCase(MathTest)
unittest.TextTestRunner(verbosity=2).run(suite)