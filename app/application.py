#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def generate_passwords(words=4, amount=10):
    '''Generates a XKCD style password with a number of words. Returns a list of amount pass phrases '''

    # Get a list of words
    with open('words.txt') as f:
        wordlist = [word.strip().replace("'","") for word in f]

    # Return a list of passwords of strings
    passwords = [' '.join(list(np.random.choice(wordlist, words))) for i in range(amount)]
    return passwords

if __name__ == "__main__":
    print(generate_passwords())
