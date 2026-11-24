subjects = ['Maths', 'Physics', 'Python']
marks = [80, 75, 90]
import matplotlib.pyplot as plt
plt.barh(subjects, marks, color=['red', 'green', 'blue'])
plt.title("Marks")
plt.grid(True)
plt.show()