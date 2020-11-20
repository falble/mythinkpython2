# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:22:36 2019

@author: Falble
"""

# Exercise 13.4

import random

from bisect import bisect

from gutemberg import process_file


def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    hist: map from word to frequency
    """
    # TODO: This could be made faster by computing the cumulative
    # frequencies once and reusing them.

    words = []
    freqs = []
    total_freq = 0

    # make a list of words and a list of cumulative frequencies
    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    # choose a random value and find its location in the cumulative list
    x = random.randint(0, total_freq-1)
    index = bisect(freqs, x)
    return words[index]


def main():
    hist = process_file('a_christmas_carol', skip_header=True)

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()