import numpy as np


def line_func(file):
    array = []
    with open(file) as a:
        for line in a:
            try:
                line = float(line.replace(',', '.').strip())
            except ValueError:
                line = 0
            array.append(line)
    return array


x = np.array(line_func('x_array.txt'))
y = np.array(line_func('y_array.txt'))
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y)[0]

print(str(m).replace('.', ','), str(c).replace('.', ','))