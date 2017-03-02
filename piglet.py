#!/usr/bin/python
# -*- coding: utf-8 -*-

vowels = ["a","o","u","e","i","y", "å", "ä", "ö"]


def consonant(letter):
    """ Return True if the input is a consonant """
    if letter in vowels:
        return False
    else:
        return True

def pig(word):
    """ Turn the word into a pig latin word """
    word = word.lower()
    if consonant(word[0]):
        for letter in word:
            if not consonant(letter):
                pigword = word[word.find(letter):] +  word[0:word.find(letter)] + "ay"
    else:
        pigword = word + "way"
    return pigword

if __name__ == "__main__":
    word = str(raw_input("word: "))
    pigword = pig(word)
    print pigword
