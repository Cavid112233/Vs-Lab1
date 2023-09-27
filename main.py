import math
eps = 0.001
s = 0
z=1/2
i=1

while math.fabs(z)>eps:
    s=s+z
    z=z**i
    i=i+1

print("s=", s)

