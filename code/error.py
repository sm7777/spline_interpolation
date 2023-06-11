from cubic_spline import calculate_cubic_polynomial
from Bspline import Bspline_interpolate, Bspline_Function
import numpy as np

def absolute_error(meas, calc):
    return abs(meas - calc)

def relative_error(meas, calc):
    return absolute_error(meas, calc) / meas


def error(x_values, y_values, coefficients):

    abs_error = []
    rel_error = []
    for i in range(len(x_values)):
        if i == len(x_values) - 1:
            c = coefficients[i-1]
        else:
            c = coefficients[i]
        y_calc = calculate_cubic_polynomial(c, x_values[i])
        abs_error.append(absolute_error(y_values[i], y_calc))
        rel_error.append(relative_error(y_values[i], y_calc))

    return (abs_error, rel_error)

def mag_error(y_error, z_error):
    mag_error = []
    for i in range(len(y_error)):
        mag_error.append(np.sqrt(y_error[i] **2 + z_error[i] **2))
    return mag_error


"""
1. Take actual data
2. Calculate y at x using the coefficients / cubic polynomial equation
"""

def bspline_error(x,y,degree):
    abs_error = []
    rel_error = []
    res = Bspline_interpolate((x,y),degree, len(x))
    x_b, y_b = res[0]
    print(y_b)

    for i in range(len(x)):
        idx = np.argmin(np.abs(x_b - x[i]))
        abs_error.append(absolute_error(y[i], y_b[idx]))
        rel_error.append(relative_error(y[i], y_b[idx]))

    return (abs_error, rel_error)

def bspline_error2(x,y,degree):
    abs_error = []
    rel_error = []

    for i in range(len(x)):
        y_int = Bspline_Function((x,y),degree, x[i])
        abs_error.append(absolute_error(y[i], y_int))
        rel_error.append(relative_error(y[i], y_int))

    return (abs_error, rel_error)
