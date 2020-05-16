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
    T_wall = constants.T_wall_init
    AOA = 0.0523599                     # = 3 degrees   # NOTE: This should be a vector, changing over time

    # Get Flight Data
    cpmax_vec = flightData.getC_pmax()
    alt_vec = flightData.getAlt()
    mach_vec = flightData.getSpeed()    # Units: [unitless]
    time_vec = flightData.getTime()
    temp_vec = [T_wall]
    atmosData = atmos.Atmos()

    for i in range(1, len(time_vec)):
        print ("i: ", i)
        print("temp_vec: ", temp_vec)
        print("temp_vec[i-1]: ", temp_vec[i-1])
        M_inf = mach_vec[i]
        speed = calc.calc_speed(mach_vec[i], temp_vec[i-i])
        h1 = 0
        h2 = 100
        print(i)
        while not (abs(h2-h1) < 0.001):
            h1 = h2
            # Calculating Nusslet's numer
            isLaminar = True
            Re = dimensionless.calcRe(atmosData.getRho(alt_vec[i]), atmosData.getMu(alt_vec[i]), speed, constants.x_char)
            if (Re >= 10**5):
                isLaminar = False
            Pr = dimensionless.calcPr(atmosData.getMu(alt_vec[i]), constants.k, constants.c_p)
            nusslet = dimensionless.calcNusslet(Re, Pr, isLaminar)    #Args: (int, int, boolean)
            T_static = atmosData.getT_static(alt_vec[i])
            T_localstag = calc.calc_T_localstag(T_static, mach_vec[i])
            q = atmosData.getq(alt_vec[i], speed)
            # Calculating thermal conductivity at reference temperature
            P_local = calc.calc_P_local(constants.C_pmax, constants.P_inf, q, AOA)
            P_infstag = calc.calc_P_infstag(M_inf, constants.P_inf)
            if (mach_vec[i] < 1):          # If mach < 1
                P_localstag = calc.calc_P_localstag_sub(P_local, M_inf)
            else:                               # If mach >= 1
                P_localstag = calc.calc_P_localstag_super(P_infstag, M_inf)
            mach_local = calc.calc_mach_local(P_localstag, P_local)
            if (isLaminar):
                recov_fact = sqrt(Pr)
            else:
                recov_fact = Pr**(1/3)
            T_local = calc.calc_T_local(T_localstag, mach_local)
            T_recov = calc.calc_T_recov(T_local, recov_fact, mach_local)
            T_ref = calc.calc_T_ref(T_local, T_recov, T_wall)
            k_ref = calc.calc_k_ref(T_ref)
            if (i == 1):                           # Calculate h for first time step
                h2 = calc.calc_h(nusslet, k_ref, constants.dist)  # dist will be some constant (where the fiberglass begins)
            else:
                h2 = calc.calc_h(nusslet, k_ref, constants.dist)      # dist will be some constant (where the fiberglass begins)
            dt = time_vec[i]-time_vec[i-1]
            T_radref = atmosData.getT_static(alt_vec[i])
            T_wall = calc.calcTemp(h2, constants.area, T_recov, T_wall, T_radref, constants.mass, constants.emmisivity, constants.c_p, dt)
        temp_vec.append(T_wall)
        print ("Appended T_wall: ", T_wall)

    # printTable()

main()