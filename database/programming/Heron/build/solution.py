#!/usr/bin/env python
# coding: utf-8
def heron(a, x0=0.1, tol=10e-10, maxiter =1000):
    """
    applies the iteration rule according to the so -called "Heron method"
    """
    counter = 0
    # while the error is above our tolerance we do the iteration
    while abs(x0 - a**0.5) > tol:
        # print the current error
        print("Error =", abs(x0 - a**0.5))
        # perfom one step of the heron method:
        x0 = 0.5 * ((x0 ** 2 + a) / x0)
        # update the counter
        counter += 1
        if counter > maxiter:
            # stop the while loop if too many iterations
            break
        print("\n Result: sqrt(a) =", x0, "\n")
    return x0
if __name__ == "__main__":
    a = 2.
    # Choose different initial values
    x0 = [0.1, 1., 100000 , 1.3]
    for x in x0:
        print("\n x0 =", x, "\n---------------\n")
        heron(a, x0=x)
    help(heron)
