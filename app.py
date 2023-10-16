import matplotlib.pyplot as plot
import numpy as np

COLOR_MAP = 'Blues' #cool

def function(x: np.ndarray, y: np.ndarray):
    return np.cos(x) + np.sin(np.cos(y)*x)

x, y = np.meshgrid(np.linspace(0, 15, 15), np.linspace(0, 15, 15))
f = function(x, y)

figure, (ax1, ax2) = plot.subplots(1, 2, figsize=(13, 5))

ax1.contourf(x, y, f, cmap=COLOR_MAP)
ax1.set_xlabel('x', fontsize = 15)
ax1.set_ylabel('y', fontsize = 15)

ax2.axis('off')

ax = figure.add_subplot(122, projection='3d')
ax.plot_surface(x, y, f, cmap=COLOR_MAP)
ax.set_xlabel('x', fontsize = 15)
ax.set_ylabel('y', fontsize = 15)

plot.show()