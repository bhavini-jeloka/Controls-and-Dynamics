from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm
import Rotation_Matrices
import time
import RBD_Euler_Method

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), zlim=(-1.5, 1.5))


def plot_cube(a, b, c, d, e, f, g, h):  # vector points for the corners (top face clockwise, bottom face clockwise)

    plt.plot([a[0], b[0]], [a[1], b[1]], [a[2], b[2]])
    plt.plot([b[0], c[0]], [b[1], c[1]], [b[2], c[2]])
    plt.plot([c[0], d[0]], [c[1], d[1]], [c[2], d[2]])
    plt.plot([d[0], a[0]], [d[1], a[1]], [d[2], a[2]])
    plt.plot([a[0], e[0]], [a[1], e[1]], [a[2], e[2]])
    plt.plot([b[0], f[0]], [b[1], f[1]], [b[2], f[2]])
    plt.plot([c[0], g[0]], [c[1], g[1]], [c[2], g[2]])
    plt.plot([d[0], h[0]], [d[1], h[1]], [d[2], h[2]])
    plt.plot([e[0], f[0]], [e[1], f[1]], [e[2], f[2]])
    plt.plot([f[0], g[0]], [f[1], g[1]], [f[2], g[2]])
    plt.plot([g[0], h[0]], [g[1], h[1]], [g[2], h[2]])
    plt.plot([h[0], e[0]], [h[1], e[1]], [h[2], e[2]])

    return


def plot_rotated_cube(a, b, c, d, e, f, g, h, r):  # plots the cube which has been rotated according to the matrix r
    plot_square(list(r.dot(np.array(a))),
                list(r.dot(np.array(b))),
                list(r.dot(np.array(c))),
                list(r.dot(np.array(d))),
                list(r.dot(np.array(e))),
                list(r.dot(np.array(f))),
                list(r.dot(np.array(g))),
                list(r.dot(np.array(h))))
    return


def rotated_cube(a, b, c, d, e, f, g, h, r):  # rotates a cube by a rotation matrix r (i.e, rotate each edge)
    new_points = [list(r.dot(np.array(a))),
                  list(r.dot(np.array(b))),
                  list(r.dot(np.array(c))),
                  list(r.dot(np.array(d))),
                  list(r.dot(np.array(e))),
                  list(r.dot(np.array(f))),
                  list(r.dot(np.array(g))),
                  list(r.dot(np.array(h)))]
    return new_points


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
