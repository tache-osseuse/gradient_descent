import matplotlib.pyplot as plot
import numpy as np
import random
import sympy as sym

COFS = [0.123901, -1.21434e-17, -0.03561956,
                -0.01106, -0.01485585, 2.74986e-18, 0.004058974, -3.4e-18]
RANGE = 3
ACCURACY = 1.e-7

def first_function(x: np.ndarray, y: np.ndarray):
    return COFS[0] + COFS[1]*x + COFS[2]*y + COFS[3]*x**2 + COFS[4]*y**2 + COFS[5]*x**3 + COFS[6]*y**3 + COFS[7]*x*y

def second_function(x: np.ndarray, y: np.ndarray):
    return np.cos(x) + np.sin(np.cos(y)*x)

def third_function(x: np.ndarray, y: np.ndarray):
    return x**2 - y**2

def get_plot(function_id: int, point: list):
    x_s, y_s = sym.symbols('x y')
    x, y = np.meshgrid(np.linspace(-RANGE, RANGE, 2*RANGE), np.linspace(-RANGE, RANGE, 2*RANGE))
    match function_id:
        case 1:
            func = first_function(x, y)
            samp_func = COFS[0] + COFS[1]*x_s + COFS[2]*y_s + COFS[3]*x_s**2 + COFS[4]*y_s**2 + COFS[5]*x_s**3 + COFS[6]*y_s**3 + COFS[7]*x_s*y_s
        case 2:
            func = second_function(x, y)
            samp_func = sym.cos(x_s) + sym.sin(sym.cos(y_s)*x_s)
        case 3:
            func = third_function(x, y)
            samp_func = x_s**2 - y_s**2
    derivative_func_in_x = samp_func.diff(x_s)
    derivative_func_in_y = samp_func.diff(y_s)
    line = []
    movin_point = point[:]
    counter = 0
    prev_res = None
    while True:
        counter += 1
        match function_id:
            case 1:
                res = first_function(movin_point[0], movin_point[1])
            case 2:
                res = second_function(float(movin_point[0]), float(movin_point[1]))
            case 3:
                res = third_function(movin_point[0], movin_point[1])
        line.append([movin_point[:], res])
        par_x = derivative_func_in_x.subs({x_s:movin_point[0], y_s:movin_point[1]})
        par_y = derivative_func_in_y.subs({x_s:movin_point[0], y_s:movin_point[1]})
        print(movin_point)
        if -RANGE <= movin_point[0] + par_x.evalf() <= RANGE: 
            movin_point[0] += par_x.evalf()
        if -RANGE <= movin_point[1] + par_y.evalf() <= RANGE: 
            movin_point[1] += par_y.evalf()
        if prev_res == None:
            prev_res = res
        else:
            if res - prev_res < ACCURACY:
                break
            else:
                prev_res = res
    print(f'func = {res}, prev_func = {prev_res}')
    return {'x_range': x, 'y_range': y, 'func_values': func, 'line': line, 
            'mp': movin_point, 'res': res, 'counter': counter}



