import random

'''
rows and cols control the size of the array
target is the part of the answer for the data, this would be part of the label
trend is also part of the answer, the AI should accurately identify the target index and the trend
IDEAL is the current value that will be determined after some testing, but that will be the measured current value, this can also be a variable if needed
uncertainty is the amount of error in terms of measured by the device
spacial uncertainty is the amount of uncertainty as a grid measured, so the spread of the uncertainty through the grid
'''
def generate(rows, cols, target, trend, IDEAL, uncertainty, spacial_uncertainty):
    grid = [[0] * rows] * cols


    grid[target[0]][target[1]] = IDEAL

    trend_len = random.randint(3, 5)
    # Setting Trend
    for i in range(trend_len):
        if trend == 'UP':
            grid[target[0]][target[1] + i] = IDEAL
        elif trend == 'DOWN':
            grid[target[0]][target[1] - i] = IDEAL
        elif trend == 'LEFT':
            grid[target[0] - i][target[1]] = IDEAL
        elif trend == 'RIGHT':
            grid[target[0] + i][target[1]] = IDEAL

    # Adding Error
    row_err = random.randint(2, spacial_uncertainty)
    col_err = random.randint(2, spacial_uncertainty)

    sign = random.random() > 0.5
    err = random.random() / uncertainty

    for i in range(target[0] - row_err, target[0] + row_err):
        for j in range(target[1] - col_err, target[1] + col_err):
            sign = random.random() > 0.5
            err = random.random() / 10.0
            if sign:
                grid[i][j] += err
            else:
                grid[i][j] -= err

    return grid

print(generate(15,15, [7,7], 'UP', 0.5, 10.0, 4))