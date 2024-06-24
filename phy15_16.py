import numpy as np
import math
# Sound Intensity Level 57.2

I0 = 4.7 * 1000
r = 37.9
I = I0 / r**3

dB = 10 * (math.log10(I/10**-12))/2
print(dB)

# Attenuation 70.7928
I0 = 0.18
a = 0.026
r = 48.2
r0 = 1.0
N = 2

Ir = I0 * np.exp(-a * (r-r0)) * (r0**2/r**2)**(N-1) * 1000
print(Ir)
