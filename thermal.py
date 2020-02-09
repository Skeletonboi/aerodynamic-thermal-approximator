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
    # q = 0.148   # Dynamic Pressure
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
import dimensionless

def main ():
    # Define all constants
    x_char = constants.getx_char()
    k = constants.getk()
    c_p = constants.getc_p()
    T_wall = constants.getT_wall()  # Initial Wall Temp

    # Get Flight Data
    alt_vec = flightData.getAlt()
    speed_vec = flightData.getSpeed()
    time_vec = flightData.getTime()
    temp_vec = [T_wall]
    atmosData = atmos.Atmos() # Check if this is instantiating class properly

    for i in range(0, len(time_vec)):
        # Calculating Nu
        isLaminar = True
        Re = dimensionless.calcRe(atmosData.getRho(alt_vec[i]), atmosData.getMu(alt_vec[i]), speed_vec[i], x_char)
        if (Re >= 10**5):
            isLaminar = False
        Pr = dimensionless.calcPr(atmosData.getMu(alt_vec[i]), k, c_p)
        Nu = dimensionless.calcNu(Re, Pr, isLaminar)    #Args: (int, int, boolean)
        T_localstag = atmosData.getT_localstag(alt_vec[i])          # TODO: Add this function to atmos.py
        # Calculating thermal conductivity at reference temperature
        P_local = calc.calc_P_local(C_pmax, P_inf, q)               # Victor: How is P_local cancelling out??
        P_infstag = calc.calc_P_infstag(M_inf)                      # Victor: How is M_inf different from the mach num? Which one uses the speed vector we're given?
        if (speed_vec[i]/343 < 1):          # If mach < 1
            P_localstag = calc.calc_P_localstag_sub(P_local, P_infstag, M_inf)
        else:                               # If mach >= 1
            P_localstag = calc.calc_P_localstag_super(P_infstag, M_inf)
        mach_local = calc.calc_mach_local(P_localstag, P_local)
        if (isLaminar):
            recov_fact = sqrt(Pr)
        else:
            recov_fact = Pr**(1/3)
        T_local = calc.calc_T_local(T_localstag, mach_local)
        T_recov = calc.calc_T_recov(recov_fact, mach_local)
        T_ref = calc.calc_T_ref(T_local, T_recov)
        k_ref = calc.calc_k_ref(T_ref)
        if (i == 0):                        # Calculate h for first time step
            h1 = calc.calc_h(Nu, k_ref, dist)  # dist will be some constant
        T_wall = calcTemp()
        temp_vec.append(T_wall)

    printTable()

def calcTemp (...):
    h2 = calc.calc_h()              # Won't this always be equal to h1??
    while (abs(h2-h1) >= 0.001):
