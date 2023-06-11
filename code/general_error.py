import error
import data_generator
import plotting
import cubic_spline
import math
import matplotlib.pyplot as plt

#coordinates = data_generator.generate_coordinates(10, 2, 1, 100)

numPoints = [5,10,20,50,100,200,300,500]
avgAbsError = []
avgRelError = []

mode = 1
degree = 2

for n in numPoints:
    currSumAbs = 0
    currSumRel = 0
    for i in range(10):

        coordinates = data_generator.generate_coordinates(n, 2, 1, 100)

        #Cubic Splines
        if mode == 0:
            title = "Cubic Splines"
            xy_coefs = cubic_spline.cubic_interpolation(coordinates[0],coordinates[1])
            xz_coefs = cubic_spline.cubic_interpolation(coordinates[0],coordinates[2])
            err_y = error.error(coordinates[0], coordinates[1], xy_coefs)
            err_z = error.error(coordinates[0], coordinates[2], xz_coefs)

        # B-Splines
        elif mode == 1:
            title = "B-Splines of Deg. " + str(degree)
            err_y = error.bspline_error2(coordinates[0], coordinates[1], int(degree))
            err_z = error.bspline_error2(coordinates[0], coordinates[2], int(degree))

        absError_y = sum(err_y[0]) / len(err_y[0])
        relError_y = sum(err_y[1]) / len(err_y[1])
        absError_z = sum(err_z[0]) / len(err_z[0])
        relError_z = sum(err_z[1]) / len(err_z[1])
        absError_3D = math.sqrt(absError_y ** 2 + absError_z ** 2)
        relError_3D = math.sqrt(relError_y ** 2 + relError_z ** 2)
        currSumAbs += absError_3D
        currSumRel += relError_3D

    avgAbsError.append(currSumAbs / 10)
    avgRelError.append((currSumRel / 10)*100)

#print(avgAbsError)
#print(avgAbsError)

absErrorLog = plotting.semi_log(numPoints, avgAbsError, "Avg. Abs. Error for " + title, "Number of Points", "log(error)")
absError = plotting.basic_plot(numPoints, avgAbsError, "Average Absolute Error for " + title, "Number of Points", "Absolute Error")
absErrorLog.savefig('plots/avgAbsErrorLog.png')
absError.savefig('plots/avAbsError.png')

relErrorLog = plotting.semi_log(numPoints, avgRelError, "Avg. Rel. Error for " + title, "Number of Points", "log(error)")
relError = plotting.basic_plot(numPoints, avgRelError, "Average Relative Error for " + title, "Number of Points", "Relative Error (%)")
relErrorLog.savefig('plots/avgRelErrorLog.png')
relError.savefig('plots/avgRelError.png')


    


