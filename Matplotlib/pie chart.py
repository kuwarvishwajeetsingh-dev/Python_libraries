import matplotlib.pyplot as plt
labels = ['Python', 'Java', 'C++']
sizes = [50, 30, 20]
plt.pie(sizes, labels=labels, autopct='%1.0f%%')
plt.show()
print("Pie chart with percentage values")
plt.pie(sizes, labels=labels, autopct='%1.0f%%',
        colors=['gold', 'skyblue', 'lightgreen'],
        explode=[0.4, 0, 0],      # pulls Python slice out
        startangle=90)            # rotates where the first slice starts
plt.title("Language Share")
plt.show()