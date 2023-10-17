import matplotlib.pyplot as plot
import numpy as np
import random
import sympy as sym

COFS = [-0.00673, 0.852442154, 0.86223302,
                0, 0.00050127,-0.08829, -0.093122603, -0.0038]

def function(x: np.ndarray, y: np.ndarray):
    # return np.cos(x) + np.sin(np.cos(y)*x)
    # return x**2 - y**2
    return COFS[0] + COFS[1]*x + COFS[2]*y + COFS[3]*x**2 + COFS[4]*y**2 + COFS[5]*x**3 + COFS[6]*y**3 + COFS[7]*x*y

COLOR_MAP = 'cool'
RANGE = 20
ITERATIONS = 1000
STEP = 0.001
line = []

x_s, y_s = sym.symbols('x y')
x, y = np.meshgrid(np.linspace(-RANGE, RANGE, 2*RANGE), np.linspace(-RANGE, RANGE, 2*RANGE))
f = function(x, y)
#samp_func = sym.cos(x_s) + sym.sin(sym.cos(y_s)*x_s)
#samp_func = x_s**2 - y_s**2
samp_func = COFS[0] + COFS[1]*x_s + COFS[2]*y_s + COFS[3]*x_s**2 + COFS[4]*y_s**2 + COFS[5]*x_s**3 + COFS[6]*y_s**3 + COFS[7]*x_s*y_s
derivative_func_in_x = samp_func.diff(x_s)
derivative_func_in_y = samp_func.diff(y_s)

point = [random.uniform(-RANGE, RANGE), random.uniform(-RANGE, RANGE)]
movin_point = point[:]
for _ in range(ITERATIONS):
    line.append([movin_point[:], function(movin_point[0], movin_point[1])])
    par_x = derivative_func_in_x.subs({x_s:movin_point[0], y_s:movin_point[1]})
    par_y = derivative_func_in_y.subs({x_s:movin_point[0], y_s:movin_point[1]})
    if -RANGE <= movin_point[0] + STEP*par_x.evalf() <= RANGE: movin_point[0] += STEP*par_x.evalf()
    if -RANGE <= movin_point[1] + STEP*par_y.evalf() <= RANGE: movin_point[1] += STEP*par_y.evalf()
figure, (ax1, ax2) = plot.subplots(1, 2, figsize=(13, 5))

ax1.contourf(x, y, f, cmap=COLOR_MAP)
ax1.set_xlabel('x', fontsize = 15)
ax1.set_ylabel('y', fontsize = 15)
ax1.scatter(point[0], point[1], c = 'red', marker = '.', s=175)
ax1.scatter(movin_point[0], movin_point[1], c = 'red', marker = '.', s=175)
ax1.plot([point[0][0] for point in line], [point[0][1] for point in line], c='red', linestyle='dashed')

ax2.axis('off')

ax = figure.add_subplot(122, projection='3d')
ax.plot_surface(x, y, f, cmap=COLOR_MAP)
ax.set_xlabel('x', fontsize = 15)
ax.set_ylabel('y', fontsize = 15)
ax.scatter(point[0], point[1], function(float(point[0]), float(point[1])), c = 'red', marker = '*', s=175)
# ax.plot([point[0][0] for point in line], [point[0][1] for point in line], [point[1] for point in line], '.-', c = 'red')

plot.show()