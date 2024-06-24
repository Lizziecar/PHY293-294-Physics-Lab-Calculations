#Imports
import numpy as np
import matplotlib.pyplot as plt
from pylab import loadtxt

#Uncertainties
def uncertainty_sum(dx, dy):
	return np.sqrt(dx**2 + dy**2)

def uncertainty_prod(x, dx, y, dy, z):
	return np.sqrt((dx/x)**2 + (dy/y)**2) * z

square_velo = np.array([0.1445572145,
						0.1980615039,
						0.1491878774,
						0.1579962035,
						0.1305142261,
						0.1031832485,
						0.1183839027,
						0.1031832485,
						0.13378589,
						0.1710325261,
						0.1268398957,
						0.1636838655])

square_length = np.array([28.72,
						39.35,
						29.64,
						31.39,
						25.93,
						20.5,
						23.52,
						20.5,
						26.58,
						33.98,
						25.2,
						32.52])

square_length_error = np.array([0.05 * 0.6427561383] * 12)

square_width = np.array([232.8384111] * 3 + [578.5640828] * 9)
square_width_error = np.array([0.05 * 0.6427561383] * 12)

square_velo_error = uncertainty_prod(square_length, square_length_error, square_width, square_width_error, square_velo)
#print(square_velo_error)



venturi_velo = np.array([0.524675731,
				0.4315080252,
				0.3447838909,
				0.2401022622,
				0.2323911029,
				0.1667934325,
				0.1535893926,
				0.1013542106])
venturi_velo_error = np.array([0.05 * 0.6427726642] * 8)
venturi_width = np.array([142.2841569,
				170.0776469,
				257.289042,
				349.9832879,
				349.9832879,
				514.6937831,
				590.5409575,
				662.5636345])
venturi_width_error = np.array([0.05 * 0.6427726642] * 8)
venturi_w_v = np.array([74.65304405,
				73.38986955,
				88.70911698,
				84.03177917,
				81.33300227,
				85.84754277,
				90.70082694,
				67.15361412])

venturi_w_v_error = uncertainty_prod(venturi_velo, venturi_velo_error, venturi_width, venturi_width_error, venturi_w_v)
print(venturi_w_v_error)

venturi_error = sum(venturi_w_v_error) / len(venturi_w_v_error)
print(venturi_error)