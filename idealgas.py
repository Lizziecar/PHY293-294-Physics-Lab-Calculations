#Volume ratio calculation
print("Volume Ratio Calculation:")

print("Method 1: Fast rate")
t1 = 23.5 + 273.15 #kelvin
t2 = 22.5 + 273.15 #kelvin
teq = 25 + 273.15 #kelvin
p1 = 38 #PSI
p2 = -2.7 #PSI
peq = 24 #PSI

v1_v2 = (t1*(peq*t2-p2*teq))/(t2*(teq*p1 - peq*t1))

print(f'V1 / V2 = {v1_v2}') 

print("Method 2: Slow rate")
t1 = 24 + 273.15 #kelvin
t2 = 22.5 + 273.15 #kelvin
teq = 24 + 273.15 #kelvin
p1 = 38.9 #PSI
p2 = -2.5 #PSI
peq = 25 #PSI

v1_v2 = (t1*(peq*t2-p2*teq))/(t2*(teq*p1 - peq*t1))
print(f'V1 / V2 = {v1_v2}') 