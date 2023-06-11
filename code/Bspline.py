import numpy as np
from scipy import interpolate

import matplotlib.pyplot as plt

def Bspline_interpolate(datapoints, degree, num_points):
 
    if(len(datapoints) == 2):
        x = datapoints[0]
        y = datapoints[1]

        tck,u = interpolate.splprep([x,y],k=degree,s=0)
    else:
        x = datapoints[0]
        y = datapoints[1]
        z = datapoints[2]
        tck,u = interpolate.splprep([x,y,z],k=degree,s=0)
    
    u=np.linspace(0,1,num=num_points,endpoint=True)
    
    return (interpolate.splev(u,tck), tck)

def Bspline_Function(datapoints, degree, x_point):
    x = datapoints[0]
    y = datapoints[1]

    tck = interpolate.splrep(x,y,k=degree,s=0)
    spline_func = interpolate.BSpline(tck[0], tck[1], tck[2])

    return spline_func(x_point)


def calculate_interpolation_error(data, degree, num_points):
    x = data[0]
    y = data[1]

    tck,u = interpolate.splprep([x,y], k=degree, s=0)
    u_interp = np.linspace(0, 1, num=num_points, endpoint=True)
    y_interp = interpolate.splev(u_interp, tck)

    y_orig = np.interp(u_interp, u, y)  # Interpolate original y-values at same u-values as the interpolated y-values

    abs_err = np.abs(y_interp - y_orig)
    rel_err = abs_err / np.abs(y_orig)

    avg_abs_err = np.mean(abs_err)
    avg_rel_err = np.mean(rel_err)

    return avg_abs_err, avg_rel_err

'''
x = np.linspace(0, 1, num=10)
y = np.random.rand(10)

degree = 3

# Generate the B-spline curve
num_points = 100
x_interp = np.linspace(x.min(), x.max(), num=num_points)
y_interp = [Bspline_Function([x, y], degree, xi) for xi in x_interp]

# Get the control points
tck = interpolate.splrep(x, y, k=degree, s=0)
x_control = tck[0]
y_control = tck[1]

# Plot the original data points, control points, and the B-spline curve
plt.plot(x, y, 'o', label='Data points')
plt.plot(x_control, y_control, 'x', label='Control points')
plt.plot(x_interp, y_interp, label='B-spline curve')
plt.legend()
plt.show()
'''





    

