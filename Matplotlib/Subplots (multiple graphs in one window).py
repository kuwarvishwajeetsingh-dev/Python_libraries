import matplotlib.pyplot as plt

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Line")

plt.subplot(2, 2, 2)
plt.bar(['A', 'B'], [5, 8])
plt.title("Bar")

plt.subplot(2, 2, 3)
plt.hist([1, 2, 2, 3, 3, 3, 4, 4, 5], bins=5, edgecolor='black')
plt.title("Histogram")

plt.subplot(2, 2, 4)
plt.pie([50, 30, 20], labels=['Py', 'Java', 'C++'])
plt.title("Pie")

plt.tight_layout()
plt.savefig("graph.png")   # call BEFORE plt.show()
plt.show()