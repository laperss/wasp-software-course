#!/usr/bin/python
# -*- coding: utf-8 -*-

consonants = "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,z".split(",")

def consonant(letter):
    """ Return True if the input is a consonant """
    return letter in consonants

def is_capitalized(word):    
    return word[0].isupper()

def title_format(word, capitalized):    
    return word.title() if capitalized else word

def pig(word):
    """ Turn the word into a pig latin word """
    capitalized = is_capitalized(word)
    word = word.lower()
    pigword = word
    if consonant(word[0]):
        for letter in word:
            if not consonant(letter):
                pigword = word[word.find(letter):] +  word[0:word.find(letter)] + "ay"
                break
    else:
        pigword = word + "way"
    return title_format(pigword, capitalized)

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
    word = str(raw_input("word: "))
    pigword = pig(word)
    print pigword

if __name__ == "__main__":
    main()
