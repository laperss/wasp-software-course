#!/usr/bin/env python3

import unittest
from piglet import *

class TestMain(unittest.TestCase):
    def test_pig(self):
        self.assertEqual(pig("linnea"), "innealay")
        self.assertEqual(pig("hallo"), "allohay")
        self.assertEqual(pig("switch"), "itchsway")
        self.assertEqual(pig("engineering"), "engineeringway")
        self.assertEqual(pig("English"), "Englishway")
        self.assertEqual(pig("I"), "Iway")
        self.assertEqual(pig("XXX"), "Xxx")
        self.assertEqual(pig("Plopp"), "Oppplay")
        self.assertEqual(pig("translation"), "anslationtray")

    def test_read_file(self):
        words = read_file("example_wordlist")
        self.assertEqual(words[0], "pig")
        self.assertEqual(words[1], "Latin")
        self.assertEqual(words[2], "banana")
        self.assertEqual(words[3], "trash")
        self.assertEqual(words[4], "happy")
        self.assertEqual(words[5], "duck")

if __name__ == "__main__" :
    unittest.main()
