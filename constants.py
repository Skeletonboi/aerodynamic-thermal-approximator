# ** Define these before running simulation **

# Dimensions [m]
x_char = 0.1
w_fiberglass = 0.1     # Length of fiberglass layer
w_epoxy = 0.2          # Length of epoxy layer
# Thermal Conductivity [J/(s*m*K)]
k = 0.4
# Specific Heat Capacity [J/g*K]
c_p = 0.4
# Max Pressure Coefficient [unitless]
C_pmax = 0.25
# Initial Altitude
alt_init = 76
# Initial Wall Temp
T_wall_init = 293
# Emmisivity of Material
emmisivity = 0.85
# Mass of Nosecone [kg]
mass = 0.100
# Gamma (valid for calorically perfect gas)
# calorically imperfect: https://www.grc.nasa.gov/WWW/BGH/stagtmp.html
# calorically perfect: https://www.grc.nasa.gov/WWW/BGH/realspec.html
gamma = 1.4
# Free-stream Pressure [Pa]
P_inf = 102000
# Distance of relevant material from the nosetip [m]
dist = 0.2
# Area of relevant material exposed to air [m^2]
area = 0.09

def getk(
        #T_wall
        ):
    # T vs k data extrapolated from: https://www.engineeringtoolbox.com/fiberglas-insulation-k-values-d_1172.html
    #k_fiberglass = (1.59*(10**(-4)))*T_wall - 0.008
    # T vs k data extrapolated from: https://www.govinfo.gov/content/pkg/GOVPUB-C13-bd8891a48757eb8f3c721febd7558612/pdf/GOVPUB-C13-bd8891a48757eb8f3c721febd7558612.pdf
    #k_epoxy = None  # INCOMPLETE
    #k_eff = (k_fiberglass*w_fiberglass + k_epoxy*w_epoxy)/(w_fiberglass + w_epoxy)

    return k
