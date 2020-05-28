import numpy as np

j = i = np.longdouble(0.0)
x0 = np.longdouble(0.6)
xStar = np.longdouble(pow(2, 1/3))

x = np.longdouble(1.4142112731933594)
y = np.longdouble(1.414215087890625)
z = np.longdouble(x+y)/2
print(z)
fz = pow(z, 2) - 2
if fz < 0:
    fz = np.format_float_scientific(fz)
    print(fz, "< 0")
else:
    fz = np.format_float_scientific(fz)
    print(fz, "> 0")
z = abs(z - np.sqrt(2))
if z <= pow(10, -6):
    z = np.format_float_scientific(z)
    print(z, ", Minimum Iterations: true")
else:
    z = np.format_float_scientific(z)
    print(z, ", Minimum Iterations: false")


#def gauss ():

    #return