import math
import Tr_calc as Tr

# Uses Eckert's reference temperature approach to iteratively calculate
# the heat transfer coefficient. An iterative method is required because
# it is a function of wall temperature.

def calc_h (gamma, aoa, q, P_inf, C_pmax, M_inf, T_localstag, T_wall, x, Re, Pr, vel, isLaminar):
    # Calculating T_local
    P_local = q*C_pmax*((cos(aoa))**2) + P_inf                              # Eq 11
    P_infstag = P_inf*((1+((gamma-1)/2*(M_inf**2)))**(gamma/(gamma-1)))     # Eq 10
    if (vel < 1):
        P_localstag = P_local*((1+(gamma/(gamma-1))*(M_inf**2))**(gamma/(gamma-1)))     # Eq 8
    else:
        factor1 = ((gamma+1)*(M_inf**2)/2)/(1+((gamma-1)/2)*(M_inf**2))
        factor2 = (2*gamma/(gamma+1))*(M_inf**2) - ((gamma-1)/(gamma+1))
        P_localstag = P_infstag*(factor1**(gamma/(gamma-1)))*(factor2**(1/(1-gamma)))   # Eq 9

    M_local = sqrt((((P_localstag/P_local)**((gamma-1)/gamma))-1)*(2/(gamma-1)))        # Eq 7
    T_local = T_stag/(1+((gamma-1)/2)*(mach_local**2))                      # Eq 13

    T_recov = Tr.get_Tr(T_localstag, gamma, isLaminar, Pr, C_pmax, aoa, P_inf, q, M_inf)
    T_ref = T_local + 0.5*(T_wall - T_local) + 0.22*(T_recov - T_local)

    if (isLaminar):
        Nu = 0.33206*sqrt(Re)*((Pr)**(1/3))
    else:
        Nu = 0.02914*(Re**0.8)*(Pr**(1/3))
