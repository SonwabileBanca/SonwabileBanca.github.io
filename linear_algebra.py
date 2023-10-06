import numpy as np
import matplotlib.pyplot as plt

# Create a sequence of numbers going from 0 to 100 in intervals of 0.5
start_val = 0
stop_val = 100
n_samples = 200
X = np.linspace(start_val, stop_val, n_samples)

params = np.array([2, -5])

"""
-----------------
Compulsory Task 1
------------------

Plot f(x) = P.X, where p is your params
"""
def generate_straight_line(X, params = np.array([2, -5])):
  X_input = np.empty((2, X.shape[0]))
  X_input[0,:] = X
  
  X_input[1,:] = 1
  print(params.shape)
  print(X_input.shape)
  return np.dot(params, X_input)

plt.figure()
plt.plot(X, generate_straight_line(X))
plt.title('Straight Line\nf(x) = 2x -5')
plt.xlabel('x')
plt.ylabel('Y')
plt.show()
