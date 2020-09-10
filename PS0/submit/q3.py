import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

A = np.load('q3-input.npy')
single_array_A = A.reshape(-1)

# Question 3 (a)
descending_A = np.sort(single_array_A)[::-1]
np.save('q3-output-sorted.npy', descending_A)
plotdata = np.tile(descending_A, (100,1))
plt.imshow(plotdata, cmap= 'gray')
plt.show()

# Question 3 (b)
plt.hist(single_array_A, bins=20)
plt.show()

# Question 3 (c)
X = A[int(len(A)/2):,:int(len(A)/2)]
np.save('q3-output-x.npy', X)
plt.imshow(X, interpolation=None, cmap="gray")
plt.show()

# Question 3 (d)
to_subtract = np.full((100,100), np.mean(A))
Y = np.subtract(A, to_subtract)
np.save('q3-output-y', Y)
plt.imshow(Y, interpolation=None, cmap="gray")
plt.show()

# Question 3 (e)
# 3 channels for RGB
Z = np.zeros((100,100,3))
# contains all indices greater than avg intensity of A
indices_required = np.argwhere(A > np.mean(A))
for index in indices_required:
    Z[index[0], index[1]] = [255, 0, 0]
img = Image.fromarray(Z.astype(np.uint8), 'RGB')
img.save('q3-output-z.png')
plt.imshow(Z, interpolation=None)
plt.show()