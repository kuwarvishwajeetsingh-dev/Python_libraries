import numpy as np

a = np.array([1, 2, 3, 4])               # 1-D
b = np.array([[1, 2, 3], [4, 5, 6]])     # 2-D (2 rows, 3 columns)

np.zeros((2, 3))        # 2x3 matrix of 0s
np.ones((2, 2))         # matrix of 1s
np.eye(3)               # 3x3 identity matrix
np.arange(0, 10, 2)     # [0 2 4 6 8]       (start, stop, step)
np.linspace(0, 1, 5)    # [0. 0.25 0.5 0.75 1.]  (5 equally spaced points)
np.random.rand(2, 2)    # random numbers between 0 and 1