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

#Initial Angle
def index_of_max(list):
	max_value = list[0]
	for i in range(len(list)):
		if list[i] > max_value:
			max_value = list[i]
			index = i;

	return index

def initial_angle(lists):
	#Only go from 40 to 80 to not hit the first peak
	check_angles = []
	start_index = 0
	for i in range(len(lists[0])):
		if lists[0][i] > 40:
			if not check_angles:
				start_index = i
			check_angles.append(lists[0][i])
	check_intesities = lists[1][start_index:] #shorten intesities accordingly

	#Get highest intesity
	max_index = index_of_max(check_intesities)
	initial_angle = check_angles[max_index]
	#print(initial_angle)

	#plt.plot(check_angles,check_intesities)
	#plt.show()

	return initial_angle

def initial_angles(arrayOfLists):
	initials = []
	for i in arrayOfLists:
		initials.append(initial_angle(i))

	return initials

t1_80 = import_data("Blackbody\\InitialAngle\\t1_80.txt")
t2_80 = import_data("Blackbody\\InitialAngle\\t2_80.txt")
t3_80 = import_data("Blackbody\\InitialAngle\\t3_80.txt")
t4_80 = import_data("Blackbody\\InitialAngle\\t4_80.txt")
t5_80 = import_data("Blackbody\\InitialAngle\\t5_80.txt")
t6_80 = import_data("Blackbody\\InitialAngle\\t6_80.txt")

initials = initial_angles([t1_80,
						   t2_80,
						   t3_80,
						   t4_80,
						   t5_80,
						   t6_80]) 

initial_angle_avg = mean_same_uncern(initials)
std_devation_intial_angle = standard_deviation(initial_angle_avg, initials)
uncertainty_initial_angle = 0.000005
print(f'Initial Angles: {initials}')
print(f'Initial Angle is: {initial_angle_avg} +/- {std_devation_intial_angle}')

trials = [1, 2, 3, 4, 5, 6]
print(trials)
#plt.plot(trials, initials)
#plt.errorbar(trials, initials, yerr=uncertainty_initial_angle, fmt = '-o')
#plt.show()

#Wien's Displacement Law
def lamda_from_angle(angle):
	A = 13900
	B = 1.689
	return np.sqrt(A/(np.sqrt(((2/np.sqrt(3))*np.sin(np.deg2rad(angle)) + 0.5)**2 + 0.75) - B))

def get_theta_peak(lists):
	theta_peaks = []
	for data in lists:
		max_index = index_of_max(data[1])
		theta_peaks.append(data[0][max_index])

	return compress_data_avg(theta_peaks)

def compress_data_avg(thetas): #cause we took 2 of each voltage
	i = 0
	new_thetas = []
	while(i < len(thetas)):
		new_thetas.append((thetas[i] + thetas[i+1])/2)
		i += 2
	return new_thetas

def temperatureOfBulb(volt,amp):
	a0 = 4.5e-3
	t0 = 20
	r0 = 1.1
	return t0 + ((volt/amp)/r0 -1)/a0

def uncern_temperature(v, uncern_v, c, uncern_c, z):
	return uncertainty_prod(v, uncern_v, c, uncern_c, z)

def wiens_law(temps, lamdas):
	return temps * (lamdas / 1e+9)

def uncern_wiens_law(temps, un_temps, lamdas, un_lamdas, wiens):
	return uncertainty_prod(temps, un_temps, lamdas, un_lamdas, wiens)

wien10_1 = import_data("Blackbody\\Wien\\10_1.txt")
wien10_2 = import_data("Blackbody\\Wien\\10_2.txt")
wien9_1 = import_data("Blackbody\\Wien\\9_1.txt")
wien9_2 = import_data("Blackbody\\Wien\\9_2.txt")
wien8_1 = import_data("Blackbody\\Wien\\8_1.txt")
wien8_2 = import_data("Blackbody\\Wien\\8_2.txt")
wien7_1 = import_data("Blackbody\\Wien\\7_1.txt")
wien7_2 = import_data("Blackbody\\Wien\\7_2.txt")
wien6_1 = import_data("Blackbody\\Wien\\6_1.txt")
wien6_2 = import_data("Blackbody\\Wien\\6_2.txt")
wien5_1 = import_data("Blackbody\\Wien\\5_1.txt")
wien5_2 = import_data("Blackbody\\Wien\\5_2.txt")
wien4_1 = import_data("Blackbody\\Wien\\4_1.txt")
wien4_2 = import_data("Blackbody\\Wien\\4_2.txt")
voltages = np.array([10, 9, 8, 7, 6, 5, 4])
currents = np.array([0.6, 0.567, 0.526, 0.487, 0.442, 0.392, 0.341])
uncern_angles_wien = np.array([0.05] * 7)
uncertainty_voltages = np.array([0.5] * 7)
uncertainty_currents = np.array([0.10] * 7)

theta_peaks = get_theta_peak([wien10_1,
							  wien10_2,
							  wien9_1,
							  wien9_2,
							  wien8_1,
							  wien8_2,
							  wien7_1,
							  wien7_2,
							  wien6_1,
							  wien6_2,
							  wien5_1,
							  wien5_2,
							  wien4_1,
							  wien4_1])
theta_actual = initial_angle_avg - theta_peaks
lamdas = lamda_from_angle(theta_actual) #in nm
#uncertainty of lamda
uncerntainty_lamdas = uncern_angles_wien
print(f'Peak Measured Angles: {theta_peaks}')
print(f'Peak Actual Measured Angles: {theta_actual}')
print(f'Wavelength values: {lamdas}')
print(f'Uncertainties: {uncerntainty_lamdas}') #uncertainty is only propgated by one variable 


#Temperature

temperatures = temperatureOfBulb(voltages, currents)
print(f'Temperature of Bulb: {temperatures}')

#uncertainty of temperature
uncerntainty_temperature = uncern_temperature(voltages, uncertainty_voltages, currents, uncertainty_currents, temperatures)
print(f'Uncern Temp: {uncerntainty_temperature}')

#Wien's law calculation
wien_values = temperatures * (lamdas / 1e+9)
wien_uncern = uncern_wiens_law(temperatures, uncerntainty_temperature, lamdas, uncerntainty_lamdas, wien_values)
avg_wien_value = mean_diff_uncern(wien_values, wien_uncern)
avg_wien_uncern = mean_same_uncern(wien_uncern)
std_dev_wien = standard_deviation(avg_wien_value, wien_values)

print(f'Wien Values: {wien_values}')
print(f'Wien Uncertainty: {wien_uncern}')

print(f'Avg Wien Value is: {avg_wien_value} +/- {std_dev_wien}')



#Testing Wavelength peaks
#datas = [wien10_1, wien10_2, 
#				 wien9_1, wien9_2,
#				 wien8_1, wien8_2, 
#				 wien7_1, wien7_2,
#				 wien6_1, wien6_2,
#				 wien5_1, wien5_2,
#				 wien4_1, wien4_2]
#lamda_data = []
#for angles in datas:
	#print(initial_angle_avg - angles[0])
#	lamda_data.append(lamda_from_angle(initial_angle_avg - angles[0]))

#print(lamda_data[0])

#for i in range(len(datas)):
#	plt.plot(lamda_data[i],datas[i][1])
#plt.xlabel("Lambda (nm)")
#plt.ylabel("Intensity (Volts)")
#plt.title("Wavelengths from Blackbody 10V to 4V")
#plt.show()


