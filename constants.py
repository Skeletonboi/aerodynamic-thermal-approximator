# ** Define these before running simulation **

# Characteristic Length [m]
x_char = None
# Thermal Conductivity
k = None
# Specific Heat Capacity
c_p = None
# Initial Altitude
alt_init = None
# Initial Wall Temp
T_wall_init = None

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