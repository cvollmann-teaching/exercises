import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # given data 
    data = np.array([[-1., 1],
                     [2, -1]])
    
    # Assembly 
    # design matrix 
    p = [0,1,2]    
    z_i = data[0,:]
    z_i = z_i[np.newaxis].T
    A = z_i**p
    
    # right-hand side
    b = data[1,:]
    
    # minimum norm least squares solution
    x_0 = linalg.lstsq(A,b)[0] # note that lstsq uses the svd
    
    # create an array of delta's in (0,1)
    num_delta = 3
    Delta = np.linspace(0.0001,1, num_delta, endpoint=False)
    
    # loop over delta's from large to small
    print("del \t x_del  \t\t\t\t\t\t    ||x_del-x0|| ||x|| \t  ||Ax-b||")
    for delta in Delta[::-1]:
        
        # solve regularized least squares problem (reg. normal equation)
        A_delta = A.T@A + delta * np.eye(len(A.T@A)) 
        x_delta = linalg.solve(A_delta, A.T@b, assume_a='pos')
        
        print(np.round(delta, 4), "\t",
              np.round(x_delta, 6), "\t",
              np.round(linalg.norm(x_delta-x_0), 6), "\t",
              np.round(linalg.norm(x_delta), 6), "\t ",
              np.round(linalg.norm(A@x_delta - b), 6))
        
        # Plot measurements and fitting curve 
        plt.figure()
        plt.title("Polynomial degree = "+str(max(p))+", delta = "+str(np.round(delta,4)))
        # mesaurements
        plt.plot(z_i, b, 'ro')
        # curve
        X = np.linspace(-2,2, 50) 
        plt.plot(X, x_delta[0] + x_delta[1]*X + x_delta[2]*(X**2), 'b')
        plt.plot(X, x_0[0] + x_0[1]*X + x_0[2]*(X**2), 'cyan', linestyle = "--")
        plt.legend(["Samples", "Regularized Sol", "MinNorm Sol"])
        plt.show()