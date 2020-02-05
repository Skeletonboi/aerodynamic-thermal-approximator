from math import sqrt, cos
# Change
#########################################################
# Aerodynamic Heating Prediction Tool for Supersonic Vehicles
#########################################################
# Design proposed by Bugra Simsek, Rocketsan Missiles Industries Inc.
# #####
# Atmospheric coefficients interpolated from U.S. Standard Atmosphere 1976
###############################################################

data = []       # Each index contains: [altitude, h]

# Data entry
h = 0.001 # Dummy placeholder global var.
constants = {
"delta":5,      # Wall Thickness
"k":6,          # Thermal Conductivity
"gamma":5       # Specific Heat Ratio of Flow
"apogee":50
"alt_init":10
}
alt = alt_init

# Altitude step
alt_step = apogee/1000

# Biot Number Check (for thin wall)
bi = h*(constants.delta/constants.k)
if bi >= 0.1:
    print("Wall cannot be modelled as thermally thin")
while (alt <= apogee):
    # Atmospheric Property Generation
    # ** INCOMPLETE **

    # Recovery Temperature Calculation
    M = 0.8     # Mach Speed to be redefined w/ profile later
    P = 0.147   # Freestream Pressure re-defined later
    q = 0.148   # Dynamic Pressure
    aoa = 2     # Degree/Rad? Re-define
    if M < 1:
        PoL = ((1+((gamma-1)/2)*(M**2))**(gamma/(gamma-1))) # Pl cancelled out
        Ml = sqrt((((PoL)**((gamma-1)/gamma))-1)*(2/(gamma-1)))
    elif M >= 1:
        Poinf = P*((1+((gamma-1/2))*(M**2))**(gamma/(gamma-1)))
        t1 = ((gamma+1)*(M**2)/2)/(1+((gamma-1)/2)*(M**2))
        t2 = (2*gamma/(gamma+gamma1))*(M**2) - ((gamma-1)/(gamma+1))
        PoL = Poinf*(t1qA**(gamma/(gamma-1)))*(t2**(1/(1-gamma)))
        Cpmax = (PoL-P)/q
        Pl = q*Cpmax *(cos(aoa)**2)+P  # [FIX] current cos is in radians
        Ml = sqrt((((PoL/Pl)**((gamma-1)/gamma))-1)*(2/(gamma-1)))

    Tl = ToL/  (1+((gamma-1)/2)*(Ml**2))
    Tr = Tl*(1+r*((gamma-1)/2)*(Ml**2))

    # Initial "h" calculation (can't we just do this before the while loop starts??)
    # ** INCOMPLETE **
    if alt == alt_init:
        # Do the calculation

    while :     # Add argument for |h^(c+1) - h^c| < 0.001
        # Temperature Calculation for Each Node
        # ** INCOMPLETE **

        # Heat Transfer Coefficient Calculation
        # ** INCOMPLETE **

    # Increment
    alt += alt_step

# Print output for all time steps
# ** INCOMPLETE **

# NEW CODE FOR MAIN FUNCTION BELOW!!
import constants
import flightData
import atmos
import calc

def main ():
    # Define all constants
    x_char = constants.getx_char()
    k = constants.getk()
    c_p = constants.getc_p()
    alt = constants.getAlt()        # Initial Altitude
    T_wall = constants.getT_wall()  # Initial Wall Temp

    # Get Flight Data
    alt_vec = flightData.getAlt()
    speed_vec = flightData.getSpeed()
    time_vec = flightData.getTime()
    temp_vec = [T_wall]
    atmosProperties = []

    for i in range(0, len(time_vec)):
        atmosProperties = atmos.getAtmos()
        Tr = calc.calcTr()
        h1 = calc.calc_h()          # First time setup for h
        T_wall = calcTemp()
        temp_vec.append(T_wall)

    printTable()

def calcTemp (...):
    h2 = calc.calc_h()              # Won't this always be equal to h1??
    while (abs(h2-h1) >= 0.001):
