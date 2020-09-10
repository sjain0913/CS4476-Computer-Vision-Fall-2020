import numpy as np

# Question 2 (a)
def random_dice(N):
    a = np.random.rand(N)
    b = (a * 5) + 1
    outcomes = np.rint(b).astype(np.uint8)
    return outcomes

# Question 2 (b)
def reshape_vector(y):
    return np.reshape(y, (3,2))

# Question 2 (c)
def max_value(z):
    max_val = np.where(z == np.max(z))
    return (max_val[0][0], max_val[1][0])

# Question 2 (d)
def count_ones(v):
    return np.count_nonzero(v == 1)