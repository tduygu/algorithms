import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
#
# plt.plot(x, y, marker='o', linestyle='-')
#
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Bla bla')
#
# plt.grid(True)
#
# plt.show()

######################################################
fig, ax = plt.subplots()

colors = ['blue', 'green', 'pink', 'white']
counts = [80, 70, 96, 15]
bar_labels = ['blue', 'green', 'pink', 'white']
bar_colors = ['tab:blue', 'tab:green', 'tab:pink', 'tab:gray']

ax.bar(colors, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('Color Counts')
ax.set_title('T-Shirt Colours')
ax.legend(title='T-shirt Colour')

plt.show()