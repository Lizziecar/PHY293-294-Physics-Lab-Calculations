import numpy as np 

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

X = [1,-1]
Wx = [[0.5, 0.5], 
	  [0, 1],
	  [1, 0]]
Wh = [-1, 0.5, 0.5]

h_before = np.dot(Wx, X)
h = sigmoid(h_before)
print(h)

z_before = np.dot(Wh, h)

a = sigmoid(np.sum(z_before))
print(a)