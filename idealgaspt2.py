print("Part 2 maths:")
#Values
dM = 24.0737
T1 = 23.5 + 273.15
T2 = 24.1 + 273.15
P1 = 6550.02 + 101325
P2 = 268206.1 + 101325

mi = (dM * T2) / (P2 * ((T1/P1) - (T2/P2)))

print(f'Initial Mass is {mi}')

#Volume
R = 0.2870
v1 = (mi* R * T1) / P1

print(f'Volume of the left tank is: {v1}')