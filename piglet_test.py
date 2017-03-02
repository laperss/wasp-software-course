import unittest
from piglet import pig

class TestMain(unittest.TestCase):
    def test_pig(self):
        self.assertEqual(pig("linnea"), "innealay")
        self.assertEqual(pig("hallo"), "allohay")
        self.assertEqual(pig("engineering"), "engineeringway")


if __name__ == "__main__" :
    unittest.main()
