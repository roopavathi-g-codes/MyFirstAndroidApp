import matplotlib.pyplot as plt
import numpy as np

# Create angle values
theta = np.linspace(0, 8 * np.pi, 1000)

# Create spiral radius
r = theta

# Convert to x and y
x = r * np.cos(theta)
y = r * np.sin(theta)

# Create color gradient
colors = theta

# Plot
plt.figure(figsize=(6,6))
plt.scatter(x, y, c=colors,cmap='hsv', s=10)
cmap='plasma'
cmap='rainbow'
cmap='cool'
s=20   # bigger dots

# Remove axes for artistic look
plt.axis('off')

# Title
plt.title("Colorful Spiral Galaxy 🌌", fontsize=14)
plt.style.use('dark_background')                                        

# Show
plt.show()
