#!/usr/bin/env python
"""
Minimalist program to exploit mars matrixes
"""
import argparse
import pandas as pd

def read_matrix(filepath_or_buffer):
    df = pd.read_csv(filepath_or_buffer, sep=' ')
    return df

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('matrix', help='path to the matrix file')

    args = ap.parse_args()

    print(read_matrix(args.matrix))

if __name__ == '__main__':
    main()
