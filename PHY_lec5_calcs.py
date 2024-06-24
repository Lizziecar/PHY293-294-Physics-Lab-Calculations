import numpy as np

#Undamped forced oscillations
print('Question 1:')
#Values
F0 = 7.54
k = 53.6
omega_omega0 = 0.58**2

C = (F0/k) / (1 - omega_omega0) * 10
print(f'Amplitude: {C} cm')

#RLC circuit
print('Question 2:')

#Values
L = 45 / 1000
C = 0.078 / 1000
R = 44
pi = np.pi

omega = np.sqrt((1/(L*C)))
freq = omega/(2*pi
print(f'Resonant Frequency: {freq}')
