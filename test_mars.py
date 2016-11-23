from mars import read_matrix
import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal

def test_read_matrix():
    index = ['GEN1', 'GEN2']
    d = {'LIB1' : pd.Series([1, 0], dtype=np.int16, index=index),
         'LIB2' : pd.Series([0, 25], dtype=np.int16, index=index),
         'LIB3' : pd.Series([0, 3], dtype=np.int16, index=index)}
    df = pd.DataFrame(d)
    assert_frame_equal(df, read_matrix("mock.txt").to_dense())

    index = ['GEN45', 'GEN2']
    d = {'LIB1' : pd.Series([1, 0], dtype=np.int16, index=index),
         'LIB2' : pd.Series([0, 25], dtype=np.int16, index=index),
         'LIB3' : pd.Series([0, 3], dtype=np.int16, index=index)}
    df = pd.DataFrame(d)
    assert not df.equals(read_matrix("mock.txt"))

    index = ['GEN1', 'GEN2']
    d = {'LIB1' : pd.Series([1, 0], dtype=np.int16, index=index),
         'LIB27' : pd.Series([0, 25], dtype=np.int16, index=index),
         'LIB3' : pd.Series([0, 3], dtype=np.int16, index=index)}
    df = pd.DataFrame(d)
    assert not df.equals(read_matrix("mock.txt"))

    index = ['GEN1', 'GEN2']
    d = {'LIB1' : pd.Series([1, 0], dtype=np.int16, index=index),
         'LIB2' : pd.Series([0, 0], dtype=np.int16, index=index),
         'LIB3' : pd.Series([0, 3], dtype=np.int16, index=index)}
    df = pd.DataFrame(d)
    assert not df.equals(read_matrix("mock.txt"))

def test_read_matrix_lib_filter():
    index = ['GEN1', 'GEN2']
    d = {'LIB1' : pd.Series([1, 0], dtype=np.int16, index=index),
         'LIB2' : pd.Series([0, 25], dtype=np.int16, index=index),
         'LIB3' : pd.Series([0, 3], dtype=np.int16, index=index)}
    df = pd.DataFrame(d)
    assert_frame_equal(df, read_matrix("mock.txt", lib_filter=r'LIB[0-9]').to_dense())

    index = ['GEN1', 'GEN2']
    d = {'LIB1' : pd.Series([1, 0], dtype=np.int16, index=index),
         'LIB3' : pd.Series([0, 3], dtype=np.int16, index=index)}

    df = pd.DataFrame(d)
    assert_frame_equal(df, read_matrix("mock.txt", lib_filter=r'LIB(1|3)').to_dense())

def test_read_matrix_feature_filter():
    index = ['GEN1', 'GEN2']
    d = {'LIB1' : pd.Series([1, 0], dtype=np.int16, index=index),
         'LIB2' : pd.Series([0, 25], dtype=np.int16, index=index),
         'LIB3' : pd.Series([0, 3], dtype=np.int16, index=index)}
    df = pd.DataFrame(d)
    assert_frame_equal(df, read_matrix("mock.txt", lib_filter=None).to_dense())

    index = ['GEN2']
    d = {'LIB1' : pd.Series([0], dtype=np.int16, index=index),
         'LIB2' : pd.Series([25], dtype=np.int16, index=index),
         'LIB3' : pd.Series([3], dtype=np.int16, index=index)}

    df = pd.DataFrame(d)
    assert_frame_equal(df, read_matrix("mock.txt", feature_filter=r'GEN(2|3)').to_dense())

