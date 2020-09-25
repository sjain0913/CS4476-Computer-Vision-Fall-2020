from skimage import feature
import numpy as np
import matplotlib.pyplot as plt
import skimage.color as color
from sklearn.cluster import MeanShift

def binReduction(im, votes, radius):
    w, h = np.shape(votes)

    out = np.zeros(shape=(w,h))

    for i in range(0, w, 10):
        for j in range(0, h, 10):
            try:
                subMatrix = votes[i-5:i+5, j-5:j+5]
                out[i,j] = np.sum(subMatrix)
            except:
                pass
    plt.title('Bin Reduction')
    plt.imshow(out)
    plt.show()

    # FIND AND DRAW CIRCLES
    centers = list()
    for i in range(w):
        for j in range(h):
            if out[i, j] >= 50:
                    centers.append((j, i))


    drawCircles(im, centers, radius)