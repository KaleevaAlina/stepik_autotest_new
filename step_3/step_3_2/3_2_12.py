import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        #self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        self.assertEqual(abs(-42), 42, "Провека на равенство  abs(-42) и 42")

    def testuroka(self):
        a=''
        for i in range(10):
            a+=str(i)
        print(a)
        self.assertEqual(a, "0123456789", "Провека на равенство 0123456789 и функции")
        
    #def test_abs2(self):
        #self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
    #    self.assertEqual(abs(-42), -42, "Провека на равенство  abs(-42) и -42")
        
if __name__ == "__main__":
    unittest.main()