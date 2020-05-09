import sys
import os
import time
import numpy as np

def test_moudle():
    print(sys.path)
    print(sys.argv)
    print(os.path)

    a = np.arange(12).reshape(3,4)
    print(a)

