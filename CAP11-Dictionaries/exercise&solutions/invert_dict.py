# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 17:46:34 2019

@author: Falble
"""

def invert_dict(d):
    """Inverts a dictionary, returning a map from val to a list of keys.
    If the mapping key->val appears in d, then in the new dictionary
    val maps to a list that includes key.
    d: dict
    Returns: dict
    """
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, z=1)
    inverse = invert_dict(d)
    for val in inverse:
        keys = inverse[val]
        print(val, keys)