#!/usr/bin/env python
"""
Minimalist program to exploit mars matrixes
"""
import argparse
import pandas as pd

def get_matrix(filepath_or_buffer):
    index = ['GEN1', 'GEN2']
    d = {'LIB1' : pd.Series([1, 0], index=index),
         'LIB2' : pd.Series([0, 25], index=index),
         'LIB3' : pd.Series([0, 3], index=index)}

    df = pd.DataFrame(d)
    return df

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('matrix', help='path to the matrix file')

    args = ap.parse()

    print(read_matrix(args.matrix))

if __name__ == '__main__':
    main()
