import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from cubic_spline import calculate_cubic_polynomial
from Bspline import Bspline_Function
from scipy import interpolate

def plot_spline2D(x_values, y_values, coefficients):

    sections = len(x_values) - 1

    '''
    coefficients = {}

    for section in range(sections):
        coefficients[section] = coef[section * 4:section * 4 + 4]
    '''
    
    fig, ax = plt.subplots()

    x_new = np.linspace(x_values[0], x_values[-1], 100*(len(x_values)-1))
    y_new = np.zeros(len(x_new))

    for region in range(len(x_values) - 1):
        coefs = coefficients[region]
        x_curr_region = np.linspace(x_values[region], x_values[region + 1], 100)
        y_curr_region = calculate_cubic_polynomial(coefs, x_curr_region)
        y_new[(region*100):(region+1)*100] = y_curr_region

    ax.plot(x_new, y_new)
    ax.scatter(x_values, y_values, color='red')
    ax.set_xlabel('x')
    ax.set_ylabel('S(x)')
    #plt.show()

    return fig

def plot_spline3D(x_values, y_values, z_values, xy_coefs, xz_coefs):
    sections = len(x_values) - 1
    
    '''
    xy_coefs = {}
    xz_coefs = {}

    for section in range(sections):
        xy_coefs[section] = xy_coef[section * 4:section * 4 + 4]
        xz_coefs[section] = xz_coef[section * 4:section * 4 + 4]
    '''

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_new = np.linspace(x_values[0], x_values[-1], 100*(len(x_values)-1))
    y_new = np.zeros(len(x_new))
    z_new = np.zeros(len(x_new))

    for region in range(len(x_values) - 1):
        xy_coefs_region = xy_coefs[region]
        xz_coefs_region = xz_coefs[region]
        x_curr_region = np.linspace(
            x_values[region], x_values[region + 1], 100)
        y_curr_region = calculate_cubic_polynomial(xy_coefs_region, x_curr_region)
        z_curr_region = calculate_cubic_polynomial(xz_coefs_region, x_curr_region)
        y_new[(region*100):(region+1)*100] = y_curr_region
        z_new[(region*100):(region+1)*100] = z_curr_region

    ax.plot(x_new, y_new, z_new)
    ax.scatter(x_values, y_values, z_values, color='red')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    #plt.show()

    return fig


import matplotlib.pyplot as plt

'''
def simple_plot(x, y):
    fig, ax = plt.subplots()

    # Plot data points
    ax.plot(x, y, 'ko', markersize=5)

    # Add dotted lines
    #ax.plot(x, y, 'k:', linewidth=0.5)

    # Add labels
    for i in range(len(x) - 1):
        x_pos = (x[i] + x[i+1]) / 2.0
        y_pos = (y[i] + y[i+1]) / 2.0
        label = f'$S_{i}$'
        ax.text(x_pos, y_pos, label, ha='center', va='center')

    p=0
    for i in range(0, len(x)):
        if i == 0 or i == len(x) - 1:
            label = f'$b_{p}$'
            p += 1
        elif i == len(x) - 2:
            label = f'$k_{i-1}$'
        else:
            label = f'$k_{i-1}$'
        ax.text(x[i], y[i], label, ha='center', va='bottom')

    # Set axis labels and limits
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(min(x)-1, max(x)+1)
    ax.set_ylim(min(y)-1, max(y)+5)

    return fig
'''

def simple_plot(x, y):
    fig, ax = plt.subplots()

    # Plot data points
    ax.plot(x, y, 'ko', markersize=5)

    # Add dotted lines
    # ax.plot(x, y, 'k:', linewidth=0.5)

    # Add labels
    for i in range(len(x) - 1):
        x_pos = (x[i] + x[i+1]) / 2.0
        y_pos = (y[i] + y[i+1]) / 2.0
        label = f'$S_{i}$'
        ax.text(x_pos, y_pos, label, ha='center', va='center')

    p = 0
    for i in range(0, len(x)):
        if i == 0 or i == len(x) - 1:
            label = f'$b_{p}$'
            p += 1
        elif i == len(x) - 2:
            label = f'$k_{i-1}$'
        else:
            label = f'$k_{i-1}$'
        ax.text(x[i], y[i], label, ha='center', va='bottom')

        # Add vertical line and shaded region
        if i != len(x) - 1:
            #ax.axvline(x=x[i], ymin=0, ymax=(y[i] / max(y)), color='black', linestyle='--', linewidth=1)
            ax.fill_betweenx(y=[0, max(y)+5], x1=x[i], x2=x[i+1], alpha=0.2)

    # Set axis labels and limits
    ax.set_title('Visualization of Variables in Cubic Splines')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(min(x)-1, max(x)+1)
    ax.set_ylim(0, max(y)+5)

    return fig

def basic_plot(x,y,title, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig

def semi_log(x,y,title, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax.semilogy(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig

def plot_3D_BSpline_WithControlPolygon(x,y,z,tck, out):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, color='red')
    ax.plot(out[0], out[1], out[2], color='blue')

    # plot control points
    ax.plot(tck[1][0], tck[1][1], tck[1][2], 'o-', color='green')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('B-Spline interpolation')

    return fig

def plot_2D_Bspline_WithControlPolygon(x,y,tck,out):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.scatter(x, y, color='red')
    ax.plot(out[0], out[1], color='blue')

    # plot control points
    ax.plot(tck[1][0], tck[1][1], 'o-', color='green')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('B-Spline interpolation')


    return fig

def plot_2D_Bspline_alternate(datapoints, degree):
    x = np.array(datapoints[0])
    y = np.array(datapoints[1])

    fig = plt.figure()
    x_interp = np.linspace(x.min(), x.max(), num=100)
    y_interp = [Bspline_Function([x, y], degree, xi) for xi in x_interp]

    # Get the control points
    tck = interpolate.splrep(x, y, k=degree, s=0)
    x_control = tck[0]
    y_control = tck[1]

    # Plot the original data points, control points, and the B-spline curve
    plt.plot(x, y, 'o', label='Data points')
    plt.plot(x_control, y_control, 'x', label='Control points')
    plt.plot(x_interp, y_interp, label='B-spline curve')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('1D B-Spline Interpolation')
    plt.legend()

    return fig

def plot_3D_Bspline_alternate(datapoints, degree):
    x = np.array(datapoints[0])
    y = np.array(datapoints[1])
    z = np.array(datapoints[2])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the original data points
    ax.scatter(x, y, z, marker='o', color='blue')

    # Interpolate the curve in x/y and x/z planes
    x_interp = np.linspace(x.min(), x.max(), num=100)
    y_interp = Bspline_Function((x,y), degree, x_interp)
    z_interp = Bspline_Function((x,z), degree, x_interp)


    ax.plot(x_interp, y_interp, z_interp, color='black')

    # Set labels for axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('2D B-Spline Interpolation')

    return fig







