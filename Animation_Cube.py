from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm
import matplotlib.animation as animation
import time
import Rotation_Matrices
import RBD_Euler_Method
import Graphing

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), zlim=(-1.5, 1.5))

# Creating an array of each corner of the cube which consists of all the vectors of the points after rotations

aa = [[0, 0, 1]]
bb = [[0, 1, 1]]
cc = [[1, 1, 1]]
dd = [[1, 0, 1]]
ee = [[0, 0, 0]]
ff = [[0, 1, 0]]
gg = [[1, 1, 0]]
hh = [[1, 0, 0]]


rotation_matrix = RBD_Euler_Method.euler_method_rotation_matrix()  # applying the Euler's equations to return rotations
k = len(rotation_matrix)


def update_cubes(i):
    plt.cla()  # the previous frame should be cleared
    # keeping the axes dimensions as constant
    ax = fig.add_subplot(111, projection='3d', xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), zlim=(-1.5, 1.5))
    # finding the position vectors of the corner of the cubes (in the ith frame)
    point_new = Graphing.rotated_cube(aa[i], bb[i], cc[i], dd[i], ee[i], ff[i], gg[i], hh[i], rotation_matrix[i])
    aa.append(point_new[0])
    bb.append(point_new[1])
    cc.append(point_new[2])
    dd.append(point_new[3])
    ee.append(point_new[4])
    ff.append(point_new[5])
    gg.append(point_new[6])
    hh.append(point_new[7])
    # returns the graph of the cube
    return Graphing.plot_cube(aa[i+1], bb[i+1], cc[i+1], dd[i+1], ee[i+1], ff[i+1], gg[i+1], hh[i+1])


# Creating the Animation object
cube_ani = animation.FuncAnimation(fig, update_cubes, frames=k, interval=1, blit=False, repeat=False)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
