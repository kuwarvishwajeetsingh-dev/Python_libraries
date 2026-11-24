import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)    # [5 7 9]
print(a * b)    # [4 10 18]   (NOT matrix multiplication) forn matrix multiplication, use np.dot(a, b) or a @ b
print(a ** 2)   # [1 4 9]
print(a * 10)   # [10 20 30]