import numpy as np
import matplotlib.pyplot as plt


def data_gen(x1, x2, m, sigma, fname=""):
    Z = np.random.uniform(-6, 6, m)
    Z.sort()
    Y = x1 + x2 * np.sin(Z)
    E = np.random.normal(0, sigma, m)
    Y += E
    data = np.vstack((Z, Y))
    if fname:
        np.save(fname, data)
    return data


def main():
    data = np.load("data_lstsq.npy")
    # = data_gen(x1=5,x2=-3, m=100, sigma=0.6,fname="data_lstsq.npy" )
    m = data.shape[1]
    Z, Y = data[0, :], data[1, :]
    plt.plot(Z, Y, 'o')

    # set up design matrix
    A = np.ones((m, 2))
    A[:, 1] = np.sin(Z)

    x, residuals, rank, singular_val = np.linalg.lstsq(A, Y, rcond=None)
    Y_fitted = x[0] + x[1] * np.sin(Z)
    plt.plot(Z.T, Y_fitted.T, "-")
    plt.show()


if __name__ == "__main__":
    main()
