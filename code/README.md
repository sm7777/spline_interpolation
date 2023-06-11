# COSC 6364 Advanced Numerical Analysis Final Project: Spline Interpolation in Three Dimensional Space

This program runs in the console and takes input from the user. The program's main functionality is generating spline interpolation plots using cubic splines and B-Splines.

To run the program:

Try:
```
python3.10 main.py
```

Or
```
python main.py
```

The program will ask for input from the user when it begins. The data is used to generate a random series of points for interpolation.

Number of coordinates: the number of data points you would like to interpolate between

x coordinate spacing: the spacing between each data point in the x-diretion e.g. x = [1,2,3,4,5] so x coordinate spacing = 1

Range of Y-values: This tells a random number generator the span of the values to create. Low is the lower bound and high is upper bound.

Example Input:
```
===================================================
COSC 6364 FINAL PROJECT: SPLINE INTERPOLATION IN 3D
===================================================
Number of Coordinates: 10
x coordinate spacing: 2
Range of Y-values:
Low: 1
High: 100
```
Output will be generated in the terminal/console reporting some error calculations. The rest of the output is a series of graphs showing the calculated interpolation trajectories. For cubic splines they are placed in /plots/cubic and for Bsplines they are in /plots/bspline

The cubic output is simply the 1D and 2D plots. For BSpline the ouput produced is for two methods of BSpline calculation and for the BSpline calculated across differing degrees.

Another file, general_error.py is included in this file set that is not used when main.py is run. This file was used for calculation of the overall error in the program. It takes data sets of size 5 up to size 500 and randomly generates coordinates. If interested in running it can be run. It takes an argument of 0 or 1 to calculate the error for cubic or bspline, respectfully. If you are running a bspline then you also need an additional argument for the degree. Examples are shown below

It will produce four plots with the calculated error. This program is fairly inefficient and execution time can take several minutes.

Cubic spline:
```
python3.10 general_error.py 0
```
or

BSpline of degree 3 (cubic)
```
python general_error.py 1 3
```