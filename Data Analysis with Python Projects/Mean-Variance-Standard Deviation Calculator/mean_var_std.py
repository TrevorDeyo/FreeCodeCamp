import numpy as np

def calculate(numbers_list):

    # check if 9 numbers
    if len(numbers_list) != 9:
        raise ValueError("List must contain nine numbers.")

    # convert python numbers_list -> numpy array -> numpy matrix
    array = np.array(numbers_list)
    matrix = array.reshape(3, 3)

    # calculate mean
    mean_axis_0 = list(np.mean(matrix, axis=0))
    mean_axis_1 = list(np.mean(matrix, axis=1))
    mean_flattened = float(np.mean(matrix))

    # calculate variance
    var_axis_0 = list(np.var(matrix, axis=0))
    var_axis_1 = list(np.var(matrix, axis=1))
    var_axis_flattened = float(np.var(matrix))

    # calculate standard deviation
    sd_axis_0 = list(np.std(matrix, axis=0))
    sd_axis_1 = list(np.std(matrix, axis=1))
    sd_flattened = float(np.std(matrix))

    # calculate max
    max_axis_0 = list(np.max(matrix, axis=0))
    max_axis_1 = list(np.max(matrix, axis=1))
    max_flattened = float(np.max(matrix))

    # calculate min
    min_axis_0 = list(np.min(matrix, axis=0))
    min_axis_1 = list(np.min(matrix, axis=1))
    min_flattened = float(np.min(matrix))

    # calculate sum
    sum_axis_0 = list(np.sum(matrix, axis=0))
    sum_axis_1 = list(np.sum(matrix, axis=1))
    sum_flattened = float(np.sum(matrix))
    
    
    calculations = {
        'mean': [mean_axis_0, mean_axis_1, mean_flattened],
        'variance': [var_axis_0, var_axis_1, var_axis_flattened],
        'standard deviation': [sd_axis_0, sd_axis_1, sd_flattened],
        'max': [max_axis_0, max_axis_1, max_flattened],
        'min': [min_axis_0, min_axis_1, min_flattened],
        'sum': [sum_axis_0, sum_axis_1, sum_flattened]
    }    
    return calculations