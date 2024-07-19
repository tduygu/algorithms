import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o', linestyle='-')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bla bla')

plt.grid(True)

plt.show()