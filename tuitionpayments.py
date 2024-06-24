total = 16968

#fall
fall_tui = 7090
fall_incid = 909.91
fall_anci = 512
fall_total = fall_tui + fall_incid + fall_anci

#winter
winter_tui = 7090
winter_incid = 911.09
winter_anci = 455
winter_total = winter_tui + winter_incid + winter_anci

#total:
real_total = fall_total + winter_total

#with osap:
fall_osap = 2749
winter_osap = 1833
new_fall_total = fall_total - fall_osap
new_winter_total = winter_total - winter_osap


#print
print(f'Fall Total: {fall_total}')
print(f'Winter Total: {winter_total}')
print(f'Year Total: {real_total}')

print("Payments:")
print(f"Fall Payment: {new_fall_total}")
print(f"Winter Payment: {new_winter_total}")
print(f"Total Payment: {new_fall_total + winter_total}")

#Dates:
from PIL import Image
img = Image.open('dates.png')
img.show()

