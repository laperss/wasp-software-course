import unittest
from piglet' import pig

class TestMain(unittest.TestCase):
    def test_pig(self):
        self.assertEqual(pig("random"), "igwordpay")


if __name__ == "__main__" :
    unittest.main()
