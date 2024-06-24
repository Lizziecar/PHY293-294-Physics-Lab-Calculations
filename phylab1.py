#Imports
import numpy as np
import matplotlib.pyplot as plt
from pylab import loadtxt

#Functions

#Uncertainties
def uncertainty_sum(dx, dy):
	return np.sqrt(dx**2 + dy**2)

def uncertainty_prod(x, dx, y, dy, z):
	return np.sqrt((dx/x)**2 + (dy/y)**2) * z

def uncertainty_full_opt1(vT, dvT, A, dA, Ri, dRi, z):
	ARi = uncertainty_prod(A, dA, Ri, dRi, (A / Ri))
	vTARI = uncertainty_sum(dvT, ARi)
	return uncertainty_prod((z/A), vTARI, A, dA, z)

def uncertainty_full_opt2(vT, dvT, A, dA, Ri, dRi, z):
	#V = dvT
	vRi = uncertainty_prod(vT, dvT, Ri, dRi, (vT / Ri))
	IvRi = uncertainty_sum(dA, vRi)
	return uncertainty_prod(vT, dvT, (A - (vT / Ri)), IvRi, z)

def uncertainty_rPower(dm, dR):
	return uncertainty_sum(dm, dR)

def import_data(filename):
	data=loadtxt(filename, usecols=(0,1,2,3,4,5), skiprows=1, unpack=True)

	return data[0], data[1], data[2], data[3], data[4], data[5]

# Least Squares
def least_squares(x, y):
	sumX = sum(x)
	sumY= sum(y)
	sumXY = sum(x*y)
	sumX2 = sum(x**2)
	N = len(x)

	m = (N * sumXY - sumX * sumY) / (N * sumX2 - (sumX**2))
	b = (sumY - m * sumX) / N

	return m, b
 	
def fitting_function_linear(x, m, b):

	return m * x + b

def lineOfBestFit(x, m, b):
	xValues = np.linspace(min(x), max(x), 100)
	yValues = fitting_function_linear(xValues, m, b)

	return xValues, yValues

# Uncertanties for m and b
def m_b_uncertainties(x, y, m, b):
	N = len(x)
	sumX = sum(x)
	sumX2 = sum(x**2)

	syx = (1 / (N-2)) * sum((y - (b + m*x))**2)
	delta = (N * sumX2) - (sumX**2)
	sm = np.sqrt(N * (syx/delta))
	sb = np.sqrt((syx * sumX2)/ delta)

	return sm, sb

# Goodness of Fit
def chi_squared(x, y, m, b, dy):
	fx = fitting_function_linear(x, m, b)
	N = len(x)

	x2 = sum(((y - fx)**2) / (dy**2))
	v = N-2

	return x2 / v

def residuals(x, y, m , b):
	fx = fitting_function_linear(x, m, b)
	resid = y - fx

	return x, resid


# Ammeter:
print("Ammeter calculations:")

# Get data
A_Ri, A_dRi, A_vT, A_dvT, A_I, A_dI = import_data("phylab1_1_4.txt") 
A_z = ((A_vT * 1000) / A_I) - A_Ri
print(f'Resistance Values: {A_z}')
avg_A_Z = sum(A_z) / len(A_z)
print(f"Avg Resistance: {avg_A_Z}")

# Uncertainties
A_R_Uncern = uncertainty_full_opt1(A_vT, A_dvT, A_I, A_dI, A_Ri, A_dRi, A_z)
print(f' Uncertainties of RA: {A_R_Uncern}')
avg_A_R_Uncern = sum(A_R_Uncern) / len(A_R_Uncern)
print(f"Avg Resistance Uncertatiy: {avg_A_R_Uncern}")

# Line of Best fit
A_m, A_b = least_squares(A_I, A_vT)
A_xVals, A_yVals = lineOfBestFit(A_I, A_m , A_b)
A_dm, A_db = m_b_uncertainties(A_I, A_vT, A_m, A_b)
print(f'Line of best fit: m = {A_m} +/- {A_dm}, b = {A_b} +/- {A_db}')

# Goodness to fit
A_chi2 = chi_squared(A_I, A_vT, A_m, A_b, A_dvT)
A_resid_x, A_resid_y = residuals(A_I, A_vT, A_m, A_b)

print(f'Goodness to Fit: Chi Squared: {A_chi2}')

# Graph: 
#Plot 1 reg graph
plt.subplot(2, 2, 1)
plt.plot(A_I, A_vT, 'o')
plt.plot(A_xVals, A_yVals)
plt.xlabel("Current I (mA)")
plt.ylabel("Voltage V (V)")
plt.title("V vs I of Ammeter")

#Plot 2 residuals
plt.subplot(2, 2, 2)
plt.plot(A_resid_x, A_resid_y, 'o')
plt.title("Residuals of Ammeter graph")

# Voltmeter
print("\n\n\n\nVoltmeter calculations:")

# Get data
Ri, dRi, vT, dvT, I, dI = import_data("phylab1_2_4.txt")
z = vT / (I - (vT / Ri))
print(f'Resistance Values: {z}')

avg_Z = sum(z) / len(z)
print(f"Avg Resistance: {avg_Z}")


# Uncertainties
R_Uncern = uncertainty_full_opt2(vT, dvT, I, dI, Ri, dRi, z)
print(f' Uncertainties of RA: {R_Uncern}')
avg_R_Uncern = sum(R_Uncern) / len(R_Uncern)
print(f"Avg Resistance Uncertatiy: {avg_R_Uncern}")

# Line of Best fit
m, b = least_squares(I, vT)
xVals, yVals = lineOfBestFit(I, m , b)
dm, db = m_b_uncertainties(I, vT, m, b)
print(f'Line of best fit: m = {m} +/- {dm}, b = {b} +/- {db}')

# Goodness to fit
chi2 = chi_squared(I, vT, m, b, dvT)
resid_x, resid_y = residuals(I, vT, m, b)

print(f'Goodness to Fit: Chi Squared: {chi2}')

# Graph: 
#Plot 3 reg graph
plt.subplot(2, 2, 3)
plt.plot(I, vT, 'o')
plt.plot(xVals, yVals)
plt.xlabel("Current I (mA)")
plt.ylabel("Voltage V (V)")
plt.title("V vs I of Voltmeter")

#Plot 2 residuals
plt.subplot(2, 2, 4)
plt.plot(resid_x, resid_y, 'o')
plt.title("Residuals of Voltmeter graph")


# Reistance of power
R1 = 1 / (A_m + (1/avg_A_Z))
R2 = avg_Z + m

uncern_R1 = uncertainty_rPower(A_dm, avg_A_R_Uncern)
uncern_R2 = uncertainty_rPower(dm, avg_R_Uncern)

print(f"\nResistance of power source: \nR1: {R1} \n R2: {R2}")
print(f'Uncertainties: \n Uncern R1: {uncern_R1} \n Uncern R2: {uncern_R2}')


plt.show()