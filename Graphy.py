import matplotlib
print("Matplotlib installed successfully!")

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("My First Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
