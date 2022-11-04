import numpy as np
import matplotlib.pyplot as plt

# the given data containing 5 measurements
data = np.array([[-2.,-1., 0., 1., 2.],
                 [-2., 1., -1., 2., 6.]])
#data = np.array([[-1., 0., 1.],
#                 [-1., 3., 1.]])
                 
# polynomial curve fitting
def poly_curve_fit(data, p, own=True):
    """
    INPUT:
        numpy.ndarray data of shape (2,m) with 
            data[0,:] = (z_1, ..., z_m) explanatory/independent variables
            data[1,:] = (y_1, ..., y_m) response/dependent variables
        list p = [p1, p2,..., pn] determining the polynomial model
            f_c(z) = c1 * z^p1 + ... + cn * z^pn 
        own : switch to use either our approach with (reduced) QR-decomposition 
              or SciPy's routine to solve the least squares problem
        
    OUTPUT:
        numpy.ndarray c of shape (n,) such that
           c = argmin_c sum_i (f_c(z_i) - y_i)^2
        
    """
    # (a) assemble the vector b
    b = data[1,:]
    
    # (b) assemble the matrix A    
    z_i = data[0,:][np.newaxis].T
    A = z_i**p
    
    # (c) determine c by solving using QR Decomposition 
    if own==True:
        # "factor_qr"
        import scipy.linalg as linalg
        Q, R = linalg.qr(A)
        m, n = len(b), len(p)
        Q, R = Q[0:m,0:n], R[0:n,0:n]
        # "solve_qr"
        c = linalg.solve_triangular(R, Q.T @ b )  
    else:
        import scipy.linalg as linalg
        c , res , rnk , s = linalg.lstsq(A,b)
        
    # (d) Plot measurements and fitting polynomial into one figure
    print("\n---------------------------\nExample: p =", p, "\nown =", own )
    Z = np.linspace(-2, 2, 50) # other z values
    Y = (Z[np.newaxis].T**p).dot(c) # evaluate model on Z
    plt.figure()
    plt.title("Polynomial degree = " + str(max(p)))
    plt.plot(z_i, b, 'ro')    
    plt.plot(Z, Y, 'b')
    plt.show()
    
    return c

if __name__ == "__main__":
    # different choices of polynomials
    P = [[1], [0,1], [0,1,2], [0, 1, 2, 3], [0, 1, 2 ,3, 4] ]
    
    # apply the routine for all those choices
    for p in P:
        for own in [True, "Scipy <lstsq>"]:
            poly_curve_fit(data, p, own = own)
        print("\n")




