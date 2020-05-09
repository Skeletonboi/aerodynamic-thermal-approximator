# ** Define these before running simulation **

# Dimensions [m]
x_char = None
w_fiberglass = None     # Length of fiberglass layer
w_epoxy = None          # Length of epoxy layer
# Thermal Conductivity
k = 0.04
# Specific Heat Capacity
c_p = None
# Initial Altitude
alt_init = 0
# Initial Wall Temp
T_wall_init = 293
# Emmisivity of Material
emmisivity = 0.85
# Mass of Nosecone [kg]
mass = 0.600
#gamma (valid for calorically perfect gas)
#calorically imperfect: https://www.grc.nasa.gov/WWW/BGH/stagtmp.html
#calorically perfect: https://www.grc.nasa.gov/WWW/BGH/realspec.html
gamma = 1.4

def getx_char():
    return x_char
def getk(
        #T_wall
        ):
    # T vs k data extrapolated from: https://www.engineeringtoolbox.com/fiberglas-insulation-k-values-d_1172.html
    #k_fiberglass = (1.59*(10**(-4)))*T_wall - 0.008
    # T vs k data extrapolated from: https://www.govinfo.gov/content/pkg/GOVPUB-C13-bd8891a48757eb8f3c721febd7558612/pdf/GOVPUB-C13-bd8891a48757eb8f3c721febd7558612.pdf
    #k_epoxy = None  # INCOMPLETE
    #k_eff = (k_fiberglass*w_fiberglass + k_epoxy*w_epoxy)/(w_fiberglass + w_epoxy)

    return k
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