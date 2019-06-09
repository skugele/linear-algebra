import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize


def plot_colspace_2d(matrix):
    if matrix.shape[0] != 2:
        raise ValueError("Matrix must have 2d column space")

    origin = np.zeros_like(matrix)

    fig, ax = plt.subplots()

    xmin, xmax = min(np.min(matrix[0]), 0), max(np.max(matrix[0]), 0)
    ymin, ymax = min(np.min(matrix[1]), 0), max(np.max(matrix[1]), 0)

    ax.axis(list(map(int, [xmin - 1, xmax + 1, ymin - 1, ymax + 1])))
    ax.grid(True)

    colors = np.linalg.norm(matrix, axis=0)
    colormap = plt.get_cmap('jet')

    norm = Normalize()
    norm.autoscale(colors)

    ax.quiver(origin[0], origin[1], matrix[0], matrix[1], scale=1, color=colormap(norm(colors)), angles='xy',
              scale_units='xy')


def plot_colspace_transform_2d(matrix, transform, showgrid=True):
    if matrix.shape[0] != 2:
        raise ValueError("Matrix must have 2d column space")

    if transform.shape != (2, 2):
        raise ValueError("Transform matrix must have shape (2,2)")

    origin = np.zeros_like(matrix)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    plt.grid(showgrid)

    colors = np.linalg.norm(matrix, axis=0)
    colormap = plt.get_cmap('jet')

    norm = Normalize()
    norm.autoscale(colors)

    trans_matrix = np.dot(transform, matrix)

    xmin, xmax = min(np.min(matrix[0]), 0), max(np.max(matrix[0]), 0)
    ymin, ymax = min(np.min(matrix[1]), 0), max(np.max(matrix[1]), 0)

    ax1.axis(list(map(int, [xmin - 1, xmax + 1, ymin - 1, ymax + 1])))
    ax1.set_title("Before")
    ax1.grid(True)
    ax1.quiver(origin[0], origin[1], matrix[0], matrix[1], color=colormap(norm(colors)), scale=1, angles='xy',
               scale_units='xy')

    xmin, xmax = min(np.min(trans_matrix[0]), 0), max(np.max(trans_matrix[0]), 0)
    ymin, ymax = min(np.min(trans_matrix[1]), 0), max(np.max(trans_matrix[1]), 0)

    ax2.axis(list(map(int, [xmin - 1, xmax + 1, ymin - 1, ymax + 1])))
    ax2.set_title("After")
    ax2.grid(True)
    ax2.quiver(origin[0], origin[1], trans_matrix[0], trans_matrix[1], color=colormap(norm(colors)), scale=1,
               angles='xy', scale_units='xy')
