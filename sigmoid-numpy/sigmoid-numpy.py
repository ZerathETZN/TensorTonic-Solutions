import numpy as np

def sigmoid(x):
    x = np.array(x)
    s = 1 / (1 + np.exp(-x))
    return s
    pass

x = [0, 2, -2]
sigmoid(x)
x = 0
sigmoid(x)
x = [[-1, 0], [1, 2]]
sigmoid(x)