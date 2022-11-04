import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt



if __name__ == "__main__":
    # generate random sample (multivariate normal distribution)
    mean = [0, 0]; cov = [[1, .7], [.7, 1]] 
    Nrandom = 100
    x = np.random.multivariate_normal(mean, cov, Nrandom).T
    
    # PCA: compute svd 
    U, sigma, V = linalg.svd(x)
    
    # least squares
    c, residuals, rank, singular_val = np.linalg.lstsq(x[0][np.newaxis].T, 
                                                       x[1], rcond=None)
    
    # PLOT
    fig, ax = plt.subplots()
    
    # plot random sample as dots
    plt.plot(x[0], x[1], "o", alpha=.6, zorder=1)
    
    # plot least squares fit: f(z) = t * c
    t = np.linspace(-3,3,20)
    plt.plot(t, t*c, zorder=4)
    print("slope of the least squares fit:", c)
    
    # plot first principal component = line spanned by first column of U
    # each point (x,y) on this line is orthogonal (-U[0,1],U[0,0])
    plt.plot(t, t*(U[0,1]/U[0,0]), zorder=4, color='red')
    print("slope of PCA line:", U[0,1]/U[0,0])
    
    # plot styling
    plt.grid( alpha = 0.25)
    plt.xlim(xmin=-3, xmax=3)
    plt.ylim(ymin=-3, ymax=3)
    ax.set_aspect('equal')
    plt.legend(["Samples", "Linear Least Squares", "First Principal Component"])
    plt.show()