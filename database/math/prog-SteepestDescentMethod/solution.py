# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import importlib

# import iterative solvers from previous build
iterSolver = importlib.import_module("prog-LinearIterations_JacRich_solution")


if __name__ == "__main__":
    # ---------------
    # PROBLEM SETUP
    # ---------------
    eigmin, eigmax = 2, 10
    A = np.array([[eigmin, 0], [0, eigmax]])
    b = np.array([0, 0])
    x = np.array([0, 0])
    x0 = np.array([4, 1.4])

    theta_max = 2./eigmax
    theta_bad = 0.99 * theta_max
    theta_opt = 2 / (eigmin+eigmax)

    # ---------------
    # METHOD SETUP
    # ---------------
    maxiter = 200
    legend = ["Richardson max", "Richardson bad", "Richardson opt",
              "Steepest Descent", "Conjugate Gradient"]
    methods = ["Richardson", "Richardson", "Richardson",
               "steepestDescent", "CG"]
    theta = [theta_max, theta_bad,  theta_opt,
             -1, -1]
    colors = ["y", "c", "b",
              "g", "r"]
    numberRuns = len(methods)

    # ---------------
    # SOLVE
    # ---------------
    X = []
    F = []
    for i, method in enumerate(methods):
        _X = iterSolver.main(A, b, x0, maxiter,
                             {method: theta[i]}, plot=0, verbose=0)[0]
        X += [np.array(_X)]
        F += [[0.5 * np.dot(x, A.dot(x)) for x in _X]]

    # ------------- #
    # plot iterates
    # ------------- #
    fig, ax = plt.subplots()
    for i, _X in enumerate(X):
        plt.plot(_X[:, 0], _X[:, 1], colors[i]+"o-")
    # add level sets
    m = 200
    for k in range(m):
        e = Ellipse(xy=np.zeros(2), width=eigmax*0.8**k,
                    height=eigmin*0.8**k, angle=0, fill=False)
        ax.add_artist(e)
    plt.legend(legend)
    plt.axis('equal')
    plt.show()
    # -------------- #
    # plot objective
    # -------------- #
    plt.figure("objective-function")
    for i, f in enumerate(F):
        plt.plot(f, colors[i]+"x-")
    plt.legend(legend)
    plt.show()
