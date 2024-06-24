#Imports
import numpy as np
import matplotlib.pyplot as plt
from pylab import loadtxt
import scipy.optimize as optimize
from scipy.stats import chisquare

def sin_function(x):
	return np.sin(x)

def chi_squared(func, x_data, y_data): # Goodness of Fit
	fx = func(x_data)
	N = len(x_data)
	sum = 0

	for i in range(N):
		#sum += (((y_data[i] - fx[i])**2) / (dy_data[i]**2))
		#print((((y_data[i] - fx[i])**2) / (dy_data[i]**2)))
		sum += (((y_data[i] - fx[i])**2) / (fx[i]))
	v = N-2

	return sum / v

x_discrete = np.linspace(0, 50, 10)
dx_discrete = np.array([100]*len(x_discrete))
x_cont = np.linspace(0,50, 1000)
y_discrete = sin_function(x_discrete)
y_cont = sin_function(x_cont)

print(x_discrete)
print(dx_discrete)

chi_value = chi_squared(sin_function, np.array(x_discrete), np.array(y_discrete), np.array(dx_discrete))
chi_value_not = chisquare(y_discrete, sin_function(x_discrete))

plt.plot(x_discrete, y_discrete, 'o')
plt.plot(x_cont, y_cont)
plt.title(f'χ^2: {chi_value_not}')
plt.show()

print(chi_value)
print(chi_value_not)

# Observations:
# Initial value is zero?
# Formula in handout is different from online formula
# Oh expected value is not the same as the function's value at the spot