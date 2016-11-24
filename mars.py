#!/usr/bin/env python
"""
Minimalist program to exploit mars matrixes
"""
import argparse
import pandas as pd
import numpy as np

def read_matrix(filepath_or_buffer, lib_filter=None, feature_filter=None):
    reader = pd.read_table(filepath_or_buffer, sep=' ',
                         chunksize=1000, na_filter=False,
                         converters={0: str}, dtype=np.uint16)

    result = _filter(next(reader), lib_filter, feature_filter)

    for temporary_df in reader:
        result = pd.concat([result, _filter(temporary_df, lib_filter, feature_filter)], axis=0)

    return result

def _filter(df, lib_filter=None, feature_filter=None):
    result = df
    if lib_filter is not None:
        result = df.filter(regex=lib_filter, axis=1)
    if feature_filter is not None:
        result = result.filter(regex=feature_filter, axis=0)
    return result


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
