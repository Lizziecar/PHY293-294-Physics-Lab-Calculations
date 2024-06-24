import numpy as np

def uncertainty_sum(dx, dy):
	return np.sqrt(dx**2 + dy**2)

def uncertainty_prod(x, dx, y, dy, z):
	return np.sqrt((dx/x)**2 + (dy/y)**2) * z

def uncertainty_full(vT, dvT, A, dA, Ri, dRi, z):
	ARi = uncertainty_prod(A, dA, Ri, dRi, z)
	vTARI = uncertainty_sum(dvT, ARi)
	return vTARI / dA

vT = np.array([6.495, 6.48, 6.462, 6.446, 6.465, 6.466])
dvT = np.array([0.0005, 0.0005, 0.0005, 0.0005 ,0.0005, 0.0005])
I = np.array([2.415, 13.863, 29.716, 63.1, 0.067, 0.248])
dI = np.array([0.0005, 0.0005, 0.005, 0.005, 0.0005, 0.0005])
Ri = np.array([2692, 465, 215.15, 99.96, 103510, 26612])
dRi = np.array([5, 5, 0.005, 0.005, 5, 5])
z = np.array([-2.559006211, 2.431291928, 2.308608157, 2.195309033, -7017.462687, -539.4193548])

Rammeter_Uncern = uncertainty_full(vT, dvT, I, dI, Ri, dRi, z)
print(f' Uncertainties of RA: {Rammeter_Uncern}')
