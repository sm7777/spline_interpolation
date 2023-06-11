import cubic_spline
import plotting
import error
import data_generator
import Bspline
from tabulate import tabulate
import matplotlib.pyplot as plt
import warnings
import os
warnings.filterwarnings("ignore", message="elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison")

print("===================================================")
print("COSC 6364 FINAL PROJECT: SPLINE INTERPOLATION IN 3D")
print("===================================================")
numcoords = input("Number of Coordinates: ")
xspace = input("x coordinate spacing: ")
print("Range of Y-values:")
y_low = input("Low: ")
y_high = input("High: ")
print("\n")

coordinates = data_generator.generate_coordinates(int(numcoords), int(xspace), int(y_low), int(y_high))

#coordinates = data_generator.generate_coordinates(10, 2, 1, 100)
#print("Coordinates Generated: ")

#print(coordinates)

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

''''
---------------------------------------------------
CUBIC SPLINE CALCULATIONS
---------------------------------------------------
'''


xy_coefs = cubic_spline.cubic_interpolation(x,y)
xz_coefs = cubic_spline.cubic_interpolation(x,z)

dir_path = 'plots/cubic'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

fig1 = plotting.plot_spline2D(x, y, xy_coefs)
fig1.savefig('plots/cubic/spline2D.png')
plt.close(fig1)

fig2 = plotting.plot_spline3D(x,y,z, xy_coefs, xz_coefs)
fig2.savefig('plots/cubic/spline3D.png')
plt.close(fig2)



'''
---------------------------------------------------
B-SPLINE CALCULATIONS
---------------------------------------------------
'''

Bspline_2D_results = []
Bspline_3D_results = []

Bspline_2D_Alt = []
Bspline_3D_Alt = []

dir_path = 'plots/bspline'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

for degree in range(1,5):
    Bspline_2D_results.append(Bspline.Bspline_interpolate((coordinates[0],coordinates[1]), degree, 100)) #2D Calculation
    Bspline_3D_results.append(Bspline.Bspline_interpolate(coordinates, degree, 100)) #3D Calculation

for i in range(0,4):
    
    out_2D = Bspline_2D_results[i][0]
    tck_2D = Bspline_2D_results[i][1]
    Bspline_2D_Plot = (plotting.plot_2D_Bspline_WithControlPolygon(x ,y, tck_2D, out_2D))
    Bspline_2D_Plot.savefig(f'plots/bspline/Bspline_2D_Plot_Degree_{i+1}.png')
    plt.close(Bspline_2D_Plot)

    out_3D = Bspline_3D_results[i][0]
    tck_3D = Bspline_3D_results[i][1]
    Bspline_3D_Plots = (plotting.plot_3D_BSpline_WithControlPolygon(x ,y, z, tck_3D, out_3D))
    Bspline_3D_Plots.savefig(f'plots/bspline/Bspline_3D_Plot_Degree_{i+1}.png')
    plt.close(Bspline_3D_Plots)
    
    #Alternate Method
    Bspline_2D_Plot_Alt = plotting.plot_2D_Bspline_alternate((x,y),i+1)
    Bspline_2D_Plot_Alt.savefig(f'plots/bspline/BsplineAlt_2D_Plot_Degree_{i+1}.png')
    plt.close(Bspline_2D_Plot_Alt)

    Bspline_3D_Plot_Alt = plotting.plot_3D_Bspline_alternate((x,y,z),i+1)
    Bspline_3D_Plot_Alt.savefig(f'plots/bspline/BsplineAlt_3D_Plot_Degree_{i+1}.png')
    plt.close(Bspline_3D_Plot_Alt)


''''
---------------------------------------------------
ERROR CALCULATION AND REPORTING
---------------------------------------------------
'''

# CUBIC SPLINE ERROR
cub_abs_error_y, cub_rel_error_y = error.error(x, y, xy_coefs)
cub_abs_error_z, cub_rel_error_z = error.error(x, z, xz_coefs)
cub_abs_mag_error = error.mag_error(cub_abs_error_y, cub_abs_error_z)
cub_rel_mag_error = error.mag_error(cub_rel_error_y, cub_rel_error_z)

# B-SPLINE ERROR
#bspline_error_2D_cubic = error.bspline_error(x,y,3)

bspline_error_1D_quadratic = error.bspline_error2(x,y,2)
bspline_error_1D_cubic = error.bspline_error2(x,y,3)
bspline_error_1D_quartic = error.bspline_error2(x,y,4)

bspline_error_1D_quadratic_z = error.bspline_error2(x,z,2)
bspline_error_1D_cubic_z = error.bspline_error2(x,z,3)
bspline_error_1D_quartic_z = error.bspline_error2(x,z,4)

bs_err_2D_quad_abs = error.mag_error(bspline_error_1D_quadratic[0], bspline_error_1D_quadratic_z[0])
bs_err_2D_cubic_abs = error.mag_error(bspline_error_1D_cubic[0], bspline_error_1D_cubic_z[0])
bs_err_2D_quartic_abs = error.mag_error(bspline_error_1D_quadratic[0], bspline_error_1D_quartic_z[0])

#print(bspline_error_2D_cubic[0])
#print(bspline_error_2D_cubic[1])
print("Cubic spline plots saved to ..\\plots\\cubic")
print("B-Spline plots saved to ..\\plots\\bspline")
print("\n")

table = [    ["Method", "AVG Abs Error", "AVG Rel Error %"],
    ["Cubic Spline 1D", sum(cub_abs_error_y)/len(x), (sum(cub_rel_error_y)/len(x))*100],
    ["Cubic Spline 2D", sum(cub_abs_mag_error)/len(x), (sum(cub_rel_mag_error)/len(x))*100],
    ["B-Spline 1D - Degree 2", sum(bspline_error_1D_quadratic[0])/len(x), (sum(bspline_error_1D_quadratic[1])/len(x))*100],
    ["B-Spline 1D - Degree 3", sum(bspline_error_1D_cubic[0])/len(x), (sum(bspline_error_1D_cubic[1])/len(x))*100],
    ["B-Spline 1D - Degree 4", sum(bspline_error_1D_quartic[0])/len(x), (sum(bspline_error_1D_quartic[1])/len(x))*100],
    ["B-Spline 2D - Degree 2", sum(bs_err_2D_quad_abs)/len(x), (sum(bs_err_2D_quad_abs)/len(x))*100],
    ["B-Spline 2D - Degree 3", sum(bs_err_2D_cubic_abs)/len(x), (sum(bs_err_2D_cubic_abs)/len(x))*100],
    ["B-Spline 2D - Degree 4", sum(bs_err_2D_quartic_abs)/len(x), (sum(bs_err_2D_quartic_abs)/len(x))*100]
]

print(tabulate(table, headers="firstrow"))
print("\n")


dir_path = 'plots/err'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

absFig_y = plotting.semi_log(x, cub_abs_error_y, "Absolute Error in Y Plane", "x", "Error")
absFig_y.savefig('plots/err/absErrorY.png')
plt.close(absFig_y)

relFig_y = plotting.semi_log(x, cub_rel_error_y, "Relative Error in Y Plane", "x", "Error")
relFig_y.savefig('plots/err/relErrorY.png')
plt.close(relFig_y)

absFig_z = plotting.semi_log(x, cub_abs_error_z, "Absolute Error in Z Plane", "x", "Error")
absFig_z.savefig('plots/err/absErrorZ.png')
plt.close(absFig_y)

relFig_z = plotting.semi_log(x, cub_rel_error_z, "Relative Error in Z Plane", "x", "Error")
relFig_z.savefig('plots/err/relErrorZ.png')
plt.close(relFig_z)




