import numpy as np
import matplotlib.pyplot as plt


# Generate a random 2x2 matrix with \rho(A)<1
A = np.random.rand(2,2)
norm_A = np.abs(np.sort(np.linalg.eig(A)[0])[-1]) # spectral radius of A
A = A/(norm_A +1)
b = np.array([0.1,0.1])

# Iteration
n = 50
X = np.zeros((n,2))
X[0] = np.random.rand(2)
for k in range(n-1):
    X[k+1] = (A@X[k]).T + b

# Test 
print("(I-A)x =",(np.eye(2)-A).dot(X[-1]),"\nb =", b)
# Plot iterates into 2d Plot
plt.plot(X[:,0], X[:,1], "ro-")
plt.axhline(0)
plt.axvline(0)
plt.show()
