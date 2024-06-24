import numpy as np
pi = np.pi

# Non dispersion
lamda1 = 1.90
lamda2 = 1.97
v = 331

k1 = (2 * pi) / lamda1
k2 = (2 * pi) / lamda2

omega1 = k1 * v
omega2 = k2 * v

omegamega = (omega1 + omega2) / 2
print(omegamega)