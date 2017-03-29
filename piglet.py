#!/usr/bin/env python3
import sys
import getopt
import re

consonants = "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,z".split(",")

def consonant(letter):
    """ Return True if the input is a consonant """
    return letter in consonants

def extract_punctuation(text):
    new_text = []
    for word in text:
        m = re.split('(\W+)',word)
        m = list(filter(None, m))
        new_text.extend(m)
    return new_text
        
def is_capitalized(word):
    return word[0].isupper()

def title_format(word, capitalized):
    return word.title() if capitalized else word

def pig(word):
    """ Turn the word into a pig latin word """
    capitalized = is_capitalized(word)
    word = word.lower()
    pigword = word
    if re.match('\W+',word) != None:
        return word

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
        lines = list(filter(None, lines))
        return lines

def translate_file(filename):
    lines = read_file(filename)
    for line in lines:
        print(pig(line))

def usage():
    print("usage: piglet.py [word1 word2 ...] [-h] [-f file]")

def main(argv):

    # Parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-f", "--file"):
            translate_file(arg)
        sys.exit()

    # Print usage if no input is provided
    if not opts and not argv:
        usage()
        sys.exit()

    # Translate input words
    if argv:
        text = extract_punctuation(argv)
        for word in text:
            print(pig(word), end=" ")
    print()

if __name__ == "__main__":
    main(sys.argv[1:])
