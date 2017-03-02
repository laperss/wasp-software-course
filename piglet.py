#!/usr/bin/python
# -*- coding: utf-8 -*-

vowels = ["a","o","u","e","i","y", "å", "ä", "ö"]

def pig(word):
    return "igwordpay"

def read_file(filename):
    with open(filename) as f:
        # Remove newlines
        lines = [line.rstrip('\n') for line in f.readlines()]
        # Remove empty strings
        lines = filter(None, lines)
        return lines

def main():
    lines = read_file("example_wordlist")
    for line in lines:
        print(pig(line))

if __name__ == "__main__":
    main()
