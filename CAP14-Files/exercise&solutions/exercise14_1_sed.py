# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:34:59 2019

@author: Falble
"""

def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    fin.close()
    fout.close()


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()