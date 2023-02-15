import numpy as np
import scipy.linalg as linalg
from scipy.sparse import linalg as spla
import scipy.sparse as sparse
import timeit


def error(approx, exact):
    return linalg.norm(approx-exact)/n


def solver_wrapper(a, b, solver="general"):
    if solver == "inv":
        a_inv = linalg.inv(a)
        return a_inv @ b
    elif solver == "general":
        return linalg.solve(a, b)
    elif solver == "spd":
        return linalg.solve(a, b, assume_a="pos")
    elif solver == "toeplitz":
        return linalg.solve_toeplitz(a[0, :], b)
    elif solver == "sparse_inv":
        a_inv = spla.inv(a)
        return a_inv @ b
    elif solver == "sparse_general":
        return spla.spsolve(a, b)
    elif solver == "cg":
        return spla.cg(a, b, maxiter=50)[0]
    else:
        raise Exception("Unknown solver")


def experiment(solver, a, b, num_runs):
    print("\nSolver:  {}".format(solver), end="\n"+"-"*25+"\n")
    wall_time = timeit.timeit('x = solver_wrapper(a,b,solver=solver)',
                              globals=globals(), number=num_runs)
    print("Time:    {:2.2f} seconds".format(wall_time))
    x = solver_wrapper(a, b, solver=solver)
    print("Error:   {:.2e}".format(error(x, exact)))


if __name__ == "__main__":

    n = 2500

    b = np.zeros(n)
    b[0], b[-1] = 1, 1
    exact = np.ones(n)

    num_runs = 5

    # DENSE
    a = -np.eye(n, k=-1) + 2 * np.eye(n) + -np.eye(n, k=1)
    solvers = ("inv", "general", "spd", "toeplitz", "cg")
    for solver in solvers:
        experiment(solver, a, b, num_runs)

    # SPARSE
    a = sparse.csr_matrix(a)
    sparse_solvers = ("sparse_inv", "sparse_general", "cg")
    for solver in sparse_solvers:
        experiment(solver, a, b, num_runs)
