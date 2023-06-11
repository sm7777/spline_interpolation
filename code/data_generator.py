import numpy as np
import random

def generate_coordinates(num_coordinates, x_spacing, y_low, y_high):
    x_values = []
    y_values = []
    z_values = []
    x_value = x_spacing

    for i in range(num_coordinates):
        x_values.append(x_value)
        x_value += x_spacing
        y_values.append(random.randint(y_low, y_high))
        z_values.append(random.randint(y_low, y_high))

    return (x_values, y_values, z_values)