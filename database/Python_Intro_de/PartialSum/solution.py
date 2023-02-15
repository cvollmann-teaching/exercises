def partial_sum(a, n):
    """
        a: python function
        n: positive integer
    """
    summe = 0
    for k in range(1, n+1):
        summe += a(k)
    return summe


if __name__ == "__main__":

    # Our example: we sum up the numbers from 1 to n
    def a(k):
        return k  # k**2

    n = 50

    # we compare to the "kleiner Gauss" (Gauss summation formula)
    print("Our result:             ", partial_sum(a, n))
    print("Gauss summation formula:", n * (n+1)//2)
