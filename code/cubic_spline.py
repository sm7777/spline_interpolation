import numpy as np

# Evaluates a value x in the cubic polynomial equation
# S(x) = ax^3 + bx^2 + cx + d
def calculate_cubic_polynomial(c, x):
    return (c[0] * (x ** 3)) + (c[1] * x ** 2) + (c[2] * x) + c[3]

def get_cubic_polynomial_constants(x):
    return [x**3, x**2, x, 1]

# To ensure continuity across points the first and second derivative of the polynomial 
# is equal where two points meet
def get_1st_der_polynomial_constants(x):
    return [3 * x**2, 2 * x, 1, 0, -(3* x ** 2), -(2 * x), -1, 0]

def get_2nd_der_polynomial_constants(x):
    return [6 * x, 2, 0, 0, -6 * x, -2, 0, 0]

# Natural Splines have the first and last points' second derivatives equal to zero
def get_boundary_constants(x):
    return [6*x, 2, 0, 0]

def solve_for_coefficients(M, A):
    I = np.linalg.inv(M)
    result = np.dot(I, A)
    return result


def cubic_interpolation(x_values, y_values):
    sections = len(x_values) - 1
    constants_matrix = [[0] * sections * 4 for _ in range(sections * 4)]
    A = [[0] * 1 for _ in range(sections * 4)] # n x 1 solution matrix

    '''
    Each section (except the last) of the dataset will generate four equations with coefficients that need to be solved
    Si(x), Si(xi+1), S'i(xi+1) = S'i+1(xi+1), S''(xi+1) = S''i+1(xi+1)
    4n coefficients will be generated
    2n Si equations
    2(n-1) S' and S'' equations
    2 boundary S''= 0 equations
    '''
    for section in range(sections):
        
        ix = section * 4

        constants_matrix[ix][ix: ix + 4] = get_cubic_polynomial_constants(x_values[section])
        constants_matrix[ix + 1][ix: ix + 4] = get_cubic_polynomial_constants(x_values[section + 1])

        A[ix] = [y_values[section]]
        A[ix + 1] = [y_values[section + 1]]

        if section != sections - 1:
            constants_matrix[ix + 2][ix: ix + 8] = get_1st_der_polynomial_constants(x_values[section + 1])
            constants_matrix[ix + 3][ix: ix + 8] = get_2nd_der_polynomial_constants(x_values[section + 1])
            A[ix + 2] = [0]
            A[ix + 3] = [0]

    bi1 = len(constants_matrix) - 2
    bi2 = len(constants_matrix) - 1
    bi2i = len(constants_matrix[0]) - 4

    constants_matrix[bi1][0:4] = get_boundary_constants(x_values[0])
    constants_matrix[bi2][bi2i:bi2i+4] = get_boundary_constants(x_values[len(x_values) - 1])

    A[len(A) - 2] = [0] 
    A[len(A) - 1] = [0]

    coefficients = solve_for_coefficients(constants_matrix, A)
    
    c = {}

    for section in range(sections):
        c[section] = coefficients[section * 4:section * 4 + 4]

    return c
