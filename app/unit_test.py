import unittest
import app

class TestPlus(unittest.TestCase):
    INT1 = 1
    INT2 = 2
    FLOAT1 = 1.4
    FLOAT2 = 2.6
    STR1 = "a"
    STR2 = "b"

    def test_int_plus_int(self):
        res = app.plus(self.INT1, self.INT2)
        print(res)
        self.assertEqual(res, {"result":self.INT1 + self.INT2})

    def test_float_plus_int(self):
        res = app.plus(self.FLOAT1, self.INT2)
        self.assertEqual(res, {"result":self.FLOAT1 + self.INT2})

    def test_float_plus_float(self):
        res = app.plus(self.FLOAT1, self.FLOAT2)
        self.assertEqual(res, {"result":self.FLOAT1 + self.FLOAT2})

    def test_int_plus_str(self):
        res = app.plus(self.INT1, self.STR1)
        self.assertEqual(res, {"result":f"Error can not perform PLUS operation between {self.INT1} and {self.STR1}"})

    def test_str_plus_int(self):
        res = app.plus(self.STR1, self.INT1)
        self.assertEqual(res, {"result":f"Error can not perform PLUS operation between {self.STR1} and {self.INT1}"})

    def test_str_plus_str(self):
        res = app.plus(self.STR1, self.STR2)
        print(res)
        self.assertEqual(res, {"result":f"Error can not perform PLUS operation between {self.STR1} and {self.STR2}"})

if __name__ == '__main__':
    unittest.main()