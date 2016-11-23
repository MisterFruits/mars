#!/usr/bin/env python
"""
Minimalist program to exploit mars matrixes
"""
import argparse
import pandas as pd

def read_matrix(filepath_or_buffer, lib_filter=None, feature_filter=None):
    df = pd.read_csv(filepath_or_buffer, sep=' ')
    if lib_filter is not None:
        print("j'adoore"+ lib_filter)
        df = df.filter(regex=lib_filter, axis=1)
    if feature_filter is not None:
        df = df.filter(regex=feature_filter, axis=0)


    return df

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('matrix', help='path to the matrix file')
    ap.add_argument('--lib-filter', '-l', help='filter library names using regex',
                    default=None)
    ap.add_argument('--feature-filter', '-f', help='filter features name using regex',
                    default=None)

    args = ap.parse_args()

    print(read_matrix(args.matrix, lib_filter=args.lib_filter,
                      feature_filter=args.feature_filter))

if __name__ == '__main__':
    main()
