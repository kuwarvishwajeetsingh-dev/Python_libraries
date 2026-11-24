import numpy as np
a = np.arange(1, 7)          # [1 2 3 4 5 6]
print(a.reshape(2, 3))       # 2 rows, 3 columns
print(a.reshape(3, 2).T)     # .T = transpose

print(np.concatenate([a, a]) )       # join arrays
m = np.array([[1, 2, 3], [4, 5, 6]])
print(np.dot(m, m.T))         # matrix multiplication