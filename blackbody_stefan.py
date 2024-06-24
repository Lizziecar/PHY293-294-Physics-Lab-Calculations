#Imports
import numpy as np
import matplotlib.pyplot as plt
from pylab import loadtxt

#Uncertainties
def uncertainty_sum(dx, dy):
	return np.sqrt(dx**2 + dy**2)

def uncertainty_prod(x, dx, y, dy, z):
	return np.sqrt((dx/x)**2 + (dy/y)**2) * z


def import_data(filename):
	data=loadtxt(filename, usecols=(0,1), skiprows=2, unpack=True)

	return data[0], data[1]

def mean_same_uncern(list):
	return sum(list)/len(list)

def standard_deviation(value, list):
	return np.sqrt((1/(len(list)-1))*sum((value - list)**2))

def mean_diff_uncern(list, uncern_list):
	return sum(list/uncern_list**2) / sum(1/uncern_list**2)

def temperatureOfBulb(volt,amp):
	a0 = 4.5e-3
	t0 = 20 + 273
	r0 = 1.1
	return t0 + ((volt/amp)/r0 -1)/a0

def uncern_temperature(v, uncern_v, c, uncern_c, z):
	return uncertainty_prod(v, uncern_v, c, uncern_c, z)

def areafromintensity(voltage, current, intensity):
	power = voltage * current
	return power / intensity


#Temperature
voltages = np.array([10, 9, 8, 7, 6, 5, 4])
uncertainty_voltages = np.array([0.5] * 7)
currents = np.array([0.604, 0.567, 0.528, 0.486, 0.437, 0.393, 0.336])
uncertainty_currents = np.array([0.10] * 7)

temperatures = temperatureOfBulb(voltages, currents)**4
uncern_temps = uncern_temperature(voltages, uncertainty_voltages, currents, uncertainty_currents, temperatures)

#Area
intensity = [0.9518, 0.836, 0.7584, 0.5382, 0.7114, 0.6614, 0.6747]
area = areafromintensity(voltages, currents, intensity)
uncern_area = uncertainty_prod(voltages, uncertainty_voltages, currents, uncertainty_currents, area)


print(area)
print(uncern_area)
plt.plot(temperatures, area)
plt.xlabel("Temperature")
plt.ylabel("Surface area of Light bulb")
plt.title("Area vs Temperture^4")
plt.show()
