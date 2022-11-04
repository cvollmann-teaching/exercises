import numpy as np
from solution import dot

def error_message(A,x):
    A_str = "A: \n" + str(A)
    x_str = "x: \n" + str(x)
    return "dot() failed for input \n" + A_str + "\n" + x_str

def test_run():
    m = 4
    n = 3
    A = np.random.rand(m, n)
    x = np.random.rand(n)

    product_numpy = A.dot(x)
    product_dot = dot(A, x)

    # print("Numpy: ", product_numpy, "\n dot_product(): ", product_dot)
    element_wise_comparison = np.isclose(product_numpy, product_dot)
    all_entries_are_close = np.all(element_wise_comparison)

    assert all_entries_are_close, error_message(A,x)

if __name__=="__main__":
    test_run()