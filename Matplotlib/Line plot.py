import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color='blue', marker='o', linestyle='--', label='Growth')
plt.title("Line Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.grid(False)
plt.show()
print("Line plot displayed successfully.")
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

plt.plot(x, [1, 2, 3, 4, 5], linestyle='-',  label="'-' solid")
plt.plot(x, [2, 3, 4, 5, 6], linestyle='--', label="'--' dashed")
plt.plot(x, [3, 4, 5, 6, 7], linestyle=':',  label="':' dotted")
plt.plot(x, [4, 5, 6, 7, 8], linestyle='-.', label="'-.' dash-dot")

plt.title("Line Styles")
plt.legend()
plt.grid(True)
plt.show()