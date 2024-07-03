import unittest
from StringValidation import emptyString

class TestStringValidation(unittest.TestCase):
    def test_lotsofgaps(self):
        self.assertEqual(emptyString("        "), True)
    
    def test_empty(self):
        self.assertEqual(emptyString(""), True)
    
    def test_appendedgaps(self):
        self.assertEqual(emptyString("mhe  "), False)
    
    def test_nogaps(self):
        self.assertEqual(emptyString("hello"), False)
    
    def test_prependedgaps(self):
        self.assertEqual(emptyString("   bye"), False)
    
    def test_random_gaps(self):
        self.assertEqual(emptyString("   b   pr   r r"), False)

if __name__ == "__main__":
    unittest.main()