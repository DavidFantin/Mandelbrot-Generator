import matplotlib.pyplot as plt
import numpy

#################################### WINDOW CONTROLS ####################################

# Window of viewing (Real axis: (x1,x2); Imaginary axis: (y1,y2))
x1 = -2.25   # Default = -2.25 
x2 = 0.75    # Default = 0.75
y1 = -1.5    # Default = -1.5
y2 = 1.5     # Default = 1.5

# Translation -> South East direction when +; North east direction when positive
SE = 0     # .5 is pretty good
NW = 0     # .5 is pretty good

# Scale factor (A > 1 zooms out; A < 1 zooms in)
A = 1      # Default = 1

#################################### BULK OF CODE ####################################

# Sets the size of the complex plane
x_values = numpy.linspace(A*x1+NW, A*x2+SE, 1000) # Horizontal divisions (real axis)
y_values = numpy.linspace(A*y1+NW, A*y2+SE, 1000) # Vertical divisions (imaginary axis)

# The sizes of the above lists
x_len = len(x_values)
y_len = len(y_values)

# Iterates through z^2 + c and returns the number of iterations
def mandel(c, max_iter):
    z = complex(0,0)
    max_iter = int(max_iter)
    for num_iter in range(max_iter):
        z = (z*z) + c
        # Check if z diverges: if the magnitude is > 4 it diverges
        if abs(z) > 4:
            break
    #number of iterations
    return num_iter

atlas = numpy.empty((x_len, y_len)) # Atlas = completed Mandelbrot Set

for i in range(x_len):
    for j in range(y_len):   
        x = x_values[i]
        y = y_values[j]
        c = complex(x,y)
                                  # Puts the number of iterations done as entries in "atlas"
        atlas[i,j] = mandel(c,40) ###########################################################
                                  # Each of which correspond to a point on the complex plane      
plt.figure(figsize = (18,18))
plt.imshow(atlas.T, interpolation="nearest")
plt.show()