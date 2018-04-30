#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def generate_xkcd_passwords(words=4, amount=10):

    # Get a list of words from the OS
    with open('/usr/share/dict/words') as f:
        wordlist = [word.strip() for word in f]

    # Return a list of passwords of strings
    passwords = [' '.join(list(np.random.choice(wordlist, words))) for i in range(amount)]
    return passwords

if __name__ == "__main__":
    print(generate_xkcd_passwords())
