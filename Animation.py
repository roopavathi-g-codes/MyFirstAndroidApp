import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Canvas
W, H = 500, 500
grid = np.zeros((H, W))

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
plt.axis('off')

img = ax.imshow(grid, cmap='magma', vmin=0, vmax=1, origin='lower')

# Particles (neurons)
N = 1200
pos = np.random.rand(N, 2) * [W, H]
vel = (np.random.rand(N, 2) - 0.5) * 2

# Center (galaxy core)
cx, cy = W/2, H/2

def animate(frame):
    global pos, vel, grid

    # Fade old trails
    grid *= 0.94

    # Rotation around center 🌌
    angle = 0.002
    cos_a, sin_a = np.cos(angle), np.sin(angle)

    for i in range(N):
        x, y = pos[i]

        # Direction to center
        dx = cx - x
        dy = cy - y
        dist = np.sqrt(dx*dx + dy*dy) + 1e-5

        # Normalize
        dx /= dist
        dy /= dist

        # Spiral motion (galaxy rotation)
        vx = vel[i][0] * cos_a - vel[i][1] * sin_a
        vy = vel[i][0] * sin_a + vel[i][1] * cos_a

        # Attraction + noise
        vx += dx * 0.3 + (np.random.rand()-0.5)*0.2
        vy += dy * 0.3 + (np.random.rand()-0.5)*0.2

        vel[i] = [vx*0.96, vy*0.96]

        # Move
        x += vel[i][0]
        y += vel[i][1]

        # Wrap edges
        x %= W
        y %= H

        pos[i] = [x, y]

        # Draw point
        xi, yi = int(x), int(y)
        grid[yi, xi] += 1

    # Glow (blur)
    grid[:] = (grid +
               np.roll(grid,1,0)+np.roll(grid,-1,0)+
               np.roll(grid,1,1)+np.roll(grid,-1,1)) / 5

    # Pulse effect 🫀
    pulse = 0.5 + 0.5*np.sin(frame*0.05)
    grid *= (0.98 + 0.02*pulse)

    # Normalize
    grid[:] = np.clip(grid, 0, 1)

    img.set_array(grid)
    return [img]

ani = FuncAnimation(fig, animate, frames=1000, interval=30)
plt.show()
