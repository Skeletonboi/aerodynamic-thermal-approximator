from math import sqrt, cos
import constants
import flightData
import atmos
import calc
import dimensionless
# Change
#########################################################
# Aerodynamic Heating Prediction Tool for Supersonic Vehicles
#########################################################
# Design proposed by Bugra Simsek, Rocketsan Missiles Industries Inc.
# #####
# Atmospheric coefficients interpolated from U.S. Standard Atmosphere 1976
###############################################################

def main ():
    # Define all constants
    x_char = constants.getx_char()
    k = constants.getk()
    c_p = constants.getc_p()
    T_wall = constants.getT_wall()  # Initial Wall Temp

    # Get Flight Data
    alt_vec = flightData.getAlt()
    mach_vec = flightData.getSpeed()    # Units: [unitless]
    time_vec = flightData.getTime()
    temp_vec = [T_wall]
    atmosData = atmos.Atmos() # Check if this is instantiating class properly

    for i in range(1, len(time_vec)):
        speed = calc.calc_speed(mach_vec[i], temp_vec[i-1])
        h1 = 0
        h2 = 100
        print(i)
        while not (abs(h2-h1) < 0.001):
            h1 = h2
            # Calculating Nu
            isLaminar = True
            Re = dimensionless.calcRe(atmosData.getRho(alt_vec[i]), atmosData.getMu(alt_vec[i]), speed, x_char)
            if (Re >= 10**5):
                isLaminar = False
            Pr = dimensionless.calcPr(atmosData.getMu(alt_vec[i]), k, c_p)
            Nu = dimensionless.calcNu(Re, Pr, isLaminar)    #Args: (int, int, boolean)
            T_static = atmosData.getT_static(alt_vec[i])
            T_localstag = calc.calc_T_localstag(T_static, speed)
            # Calculating thermal conductivity at reference temperature
            P_local = calc.calc_P_local(C_pmax, P_inf, q)               # Victor: How is P_local cancelling out??
            P_infstag = calc.calc_P_infstag(M_inf)                      # Victor: How is M_inf different from the mach num? Which one uses the speed vector we're given?
            if (mach_vec[i] < 1):          # If mach < 1
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
            T_ref = calc.calc_T_ref(T_local, T_recov, T_wall)
            k_ref = calc.calc_k_ref(T_ref)
            if (i == 1):                           # Calculate h for first time step
                h2 = calc.calc_h(Nu, k_ref, dist)  # dist will be some constant (where the fiberglass begins)
            else:
                h2 = calc.calc_h(Nu, k_ref, dist)      # dist will be some constant (where the fiberglass begins)
            dt = time_vec[i]-time_vec[i-1]
            T_wall = calc.calcTemp(h2, area, T_recov, T_wall, T_ref, constants.getMass(), constants.getEmmisivity(), constants.getc_p(), dt)
        temp_vec.append(T_wall)

    printTable()

a = main()