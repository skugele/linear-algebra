import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize


def plot_column_vectors_2d(matrix):
    """
    Plots column vectors from the supplied matrix in the 2D plane.  The matrix must have shape (2,X), where X >= 1.
    :param matrix: a (2,X) matrix; x >= 1
    :return: None.  Displays 2D plot.
    """
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


def plot_column_vectors_with_transform_2d(matrix, transform):
    """
    Displays a side-by-side plot of the column vectors in the supplied matrix and the column vectors in the transformed matrix matrix * transform.

    The matrix must have shape (2,X), where X >= 1.
    The transform must have shape (2,2)

    :param matrix: a (2,X) matrix; x >= 1
    :param transform: a (2,2) transformation matrix.
    :return: None. Displays 2 2D subplots.
    """
    if matrix.shape[0] != 2:
        raise ValueError("Matrix must have 2d column space")

    if transform.shape != (2, 2):
        raise ValueError("Transform matrix must have shape (2,2)")

    origin = np.zeros_like(matrix)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    colors = np.linalg.norm(matrix, axis=0)
    colormap = plt.get_cmap('jet')

    norm = Normalize()
    norm.autoscale(colors)

    trans_matrix = np.dot(transform, matrix)

    xmin, xmax = min(np.min(matrix[0]), 0), max(np.max(matrix[0]), 0)
    ymin, ymax = min(np.min(matrix[1]), 0), max(np.max(matrix[1]), 0)

    ax1.axis(list(map(int, [xmin - 1, xmax + 1, ymin - 1, ymax + 1])))
    ax1.set_title("$A$")
    ax1.grid(True)
    ax1.quiver(origin[0], origin[1], matrix[0], matrix[1], color=colormap(norm(colors)), scale=1, angles='xy',
               scale_units='xy')

    xmin, xmax = min(np.min(trans_matrix[0]), 0), max(np.max(trans_matrix[0]), 0)
    ymin, ymax = min(np.min(trans_matrix[1]), 0), max(np.max(trans_matrix[1]), 0)

    ax2.axis(list(map(int, [xmin - 1, xmax + 1, ymin - 1, ymax + 1])))
    ax2.set_title("$TA$")
    ax2.grid(True)
    ax2.quiver(origin[0], origin[1], trans_matrix[0], trans_matrix[1], color=colormap(norm(colors)), scale=1,
               angles='xy', scale_units='xy')
