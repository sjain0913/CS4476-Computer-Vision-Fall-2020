# Saumya Jain
import numpy as np

def compute_homography(t1, t2):
    """
    Computes the Homography matrix for corresponding image points t1 and t2

    The function should take a list of N ≥ 4 pairs of corresponding points 
    from the two views, where each point is specified with its 2d image 
    coordinates.

    Inputs:
    - t1: Nx2 matrix of image points from view 1
    - t2: Nx2 matrix of image points from view 2

    Returns a tuple of:
    - H: 3x3 Homography matrix
    """
    H = np.eye(3)
    
    points_list = []

    for i in range(0, len(t1)):
        t1_x_coordinate, t1_y_coordinate = t1[i][0], t1[i][1]
        t2_x_coordinate, t2_y_coordinate = t2[i][0], t2[i][1]
        points_list.append([t1_x_coordinate, t1_y_coordinate, 1, 0, 0, 0, -t2_x_coordinate * t1_x_coordinate, -t2_x_coordinate * t1_y_coordinate, -t2_x_coordinate])
        points_list.append([0, 0, 0, t1_x_coordinate, t1_y_coordinate, 1, -t2_y_coordinate * t1_x_coordinate, -t2_y_coordinate* t1_y_coordinate, -t2_y_coordinate])
        
    points_list = np.asarray(points_list)
    u, s, vh = np.linalg.svd(points_list)
    H = (vh[-1,:] / vh[-1,-1]).reshape(3, 3)

    return H