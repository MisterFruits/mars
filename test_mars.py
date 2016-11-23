from mars import read_matrix
import pandas as pd
from pandas.util.testing import assert_frame_equal

def test_read_matrix():
    index = ['GEN1', 'GEN2']
    d = {'LIB1' : pd.Series([1, 0], index=index),
         'LIB2' : pd.Series([0, 25], index=index),
         'LIB3' : pd.Series([0, 3], index=index)}

    df = pd.DataFrame(d)
    assert_frame_equal(df, read_matrix("mock.txt"))

    index = ['GEN45', 'GEN2']
    d = {'LIB1' : pd.Series([1, 0], index=index),
         'LIB2' : pd.Series([0, 25], index=index),
         'LIB3' : pd.Series([0, 3], index=index)}

    df = pd.DataFrame(d)
    assert not df.equals(read_matrix("mock.txt"))

    index = ['GEN1', 'GEN2']
    d = {'LIB1' : pd.Series([1, 0], index=index),
         'LIB27' : pd.Series([0, 25], index=index),
         'LIB3' : pd.Series([0, 3], index=index)}

    df = pd.DataFrame(d)
    assert not df.equals(read_matrix("mock.txt"))

    index = ['GEN1', 'GEN2']
    d = {'LIB1' : pd.Series([1, 0], index=index),
         'LIB2' : pd.Series([0, 0], index=index),
         'LIB3' : pd.Series([0, 3], index=index)}

    df = pd.DataFrame(d)
    assert not df.equals(read_matrix("mock.txt"))
