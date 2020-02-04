# ** Define these before running simulation **

# Characteristic Length [m]
x_char = NaN
# Thermal Conductivity
k = NaN
# Specific Heat Capacity
c_p = NaN
# Initial Altitude
alt_init = NaN
# Initial Wall Temp
T_wall_init = NaN

def getx_char():
    return x_char
def getk():
    return k
def getc_p():
    return c_p
def getAlt():
    return alt_init
def getT_wall():
    return T_wall_init