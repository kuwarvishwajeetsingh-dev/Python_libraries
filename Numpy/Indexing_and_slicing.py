import numpy as np
a = np.array([10, 20, 30, 40, 50])
print(a[0])        # 10
print(a[-1])       # 50
print(a[1:4])      # [20 30 40]  (stop index excluded)

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[1, 2])     # 6   -> row 1, column 2
print(b[:, 1])     # [2 5 8] -> all rows, column 1
print(b[0:2, 0:2]) # [[1 2] [4 5]]