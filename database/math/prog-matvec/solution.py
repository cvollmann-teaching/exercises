import numpy as np
import scipy.sparse as scs
import timeit


def matvec_dense(A, x, byhand=0):
    """
    computes the matrix vector product based on numpy.ndarray

    Parameters
    ----------
    A : (m,n) numpy.ndarray
       matrix
    x : (n, ) numpy.ndarray
       vector
    byhand : int
       switch between for loop and @ operator

    Returns
    -------
        A*x: matrix-vector product
    """
    if byhand:
        # read the dimensions of the input objects
        m, n = np.shape(A)
        nx = len(x)

        # raise an error if the dimensions do not match
        if n != nx:
            raise Exception('dimension of A and x must match. The dimension \
                            for A and x were: {}'.format(str(np.shape(A))
                                                         + " " + str(len(x))))

        # if dimensions match, start computing the matrix-vector product:
        else:
            # initialize the output vector
            b = np.zeros(m)
            # a loop over row indices to compute each entry of b
            for i in range(m):
                # a loop over column indices to compute the inner product
                for j in range(n):
                    b[i] += A[i, j] * x[j]
    else:
        b = A.dot(x)  # np.dot(A,x), A@x
    return b


# we could implement our own csr-class in python:
# class csr_matrix:
#    def __init__(self, data, indices, indptr):
#        self.data = data
#        self.indices = indices
#        self.indptr = indptr

def matvec_sparse(A, x, byhand=0):
    """computes the matrix vector product based on csr matrix

    Parameters
    ----------
    A: (m,n) matrix  stored in CSR, i.e., in terms of three lists; here:
       class with attributes data, indices, indptr
    x: (n, ) numpy.ndarray or list of length n (= number of cols) numbers
       vector
    byhand : int
       switch between for loop and @ operator

    Returns
    -------
        A*x: matrix-vector product
    """
    if byhand:
        # dimension check?
        # can we get the column dimension from sparse csr class? > depends
        b = [0] * (len(A.indptr) - 1)
        for i, pair in enumerate(zip(A.indptr[0:-1], A.indptr[1:])):
            for a_ij, j in zip(A.data[pair[0]:pair[1]],
                               A.indices[pair[0]:pair[1]]):
                b[i] += a_ij * x[j]
    else:
        # make sure A and x have the correct format for the dot method
        A = scs.csr_matrix(A)
        x = np.array(x)
        # compute matrix-vector product
        b = A.dot(x)
    return np.array(b)


print("\nIn order to get the docstring of our function we can type  \
      \n\n     help(functionName)\n\nFor example: ")
print(help(matvec_dense))

if __name__ == "__main__":
    # Note: the following part is only executed if the current script is
    #       run directly, but not if it is imported into another script
    # ---------------------------------------------------------------#
    #    EXPERIMENT
    # ---------------------------------------------------------------#
    # the experiment
    n = int(1e3)  # matrix column dimension
    m = n  # matrix row dimension
    runs = 50  # how many runs for time measurement
    x = np.random.rand(n)  # random vector x

    # test arrays for which we know the result
    xtest = np.ones(n)  # test input x
    btest = np.zeros(m)  # known test output b
    btest[[0, -1]] = 1

    # just some strings for printing commands
    expstr = ["Time dot:     ", "Time hand:    "]
    teststr = ["Test dot:     ", "Test by hand: "]

    # ---------------------------------------------------------------#
    #    NUMPY DENSE
    # ---------------------------------------------------------------#
    print("\n---- Numpy Dense ----")
    A = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    print("Memory:", np.round(A.nbytes * 10 ** -9, decimals=4), "Gbytes\n")
    for byhand in [0, 1]:
        print(teststr[byhand], np.allclose(btest,
                                           matvec_dense(A, xtest, byhand=byhand)))


        def dense():
            return matvec_dense(A, x, byhand=byhand)


        print(expstr[byhand], timeit.timeit("dense()",
                                            setup="from __main__ import dense", number=runs), "\n")

    # ---------------------------------------------------------------#
    #   SCIPY SPARSE
    # ---------------------------------------------------------------#
    print("\n---- Scipy Sparse ----")
    A = 2 * scs.eye(n) - scs.eye(n, k=1) - scs.eye(n, k=-1)
    print("Memory:", np.round((A.data.nbytes + A.indptr.nbytes +
                               A.indices.nbytes) * 10 ** -9, decimals=4),
          "Gbytes\n")
    for byhand in [0, 1]:
        print(teststr[byhand],
              np.allclose(btest, matvec_sparse(A, xtest, byhand=byhand)))


        def sparse():
            return matvec_sparse(A, x, byhand=byhand)


        print(expstr[byhand], timeit.timeit("sparse()",
                                            setup="from __main__ import sparse", number=runs), "\n")
