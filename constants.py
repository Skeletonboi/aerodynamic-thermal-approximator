# ** Define these before running simulation **

# Dimensions [m]
x_char = None
w_fiberglass = None     # Length of fiberglass layer
w_epoxy = None          # Length of epoxy layer
# Thermal Conductivity
k = None
# Specific Heat Capacity
c_p = None
# Initial Altitude
alt_init = None
# Initial Wall Temp
T_wall_init = None
# Emmisivity of Material
emmisivity = None
# Mass of Rocket [kg]
mass = None
#gamma
gamma = None

def getx_char():
    return x_char
def getk(T_wall):
    # T vs k data extrapolated from: https://www.engineeringtoolbox.com/fiberglas-insulation-k-values-d_1172.html
    k_fiberglass = (1.59*(10**(-4)))*T_wall - 0.008

    k_eff = (k_fiberglass*w_fiberglass + k_epoxy*w_epoxy)/(w_fiberglass + w_epoxy)
    return k_eff
def getc_p():
    return c_p
def getAlt():
    return alt_init
def getT_wall():
    return T_wall_init
def getEmmisivity():
    return emmisivity
def getMass():
    return mass
def getGamma():
    return gamma