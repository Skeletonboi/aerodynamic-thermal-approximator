import math as m
from flightData import getAOA
import constants
import numpy as np

gamma = constants.gamma

def calc_P_local(C_pmax, P_inf, q, AOA):
    #q : dynamic pressure
    #C_pmax : maximum pressure coefficient on the body surface
    #P_inf : free stream pressure
    return q*C_pmax*(m.cos(AOA)**2)+P_inf

def calc_P_infstag(M_inf, P_inf):
    #gamma : specific heat ratio of flow
    #M_inf : free stream mach number
    #P_L : Local pressure
    P_infstag = P_inf*((1+((gamma-1)/2*(M_inf**2)))**(gamma/(gamma-1)))
    return P_infstag


def calc_P_localstag_sub(P_local, M_inf):
    P_localstag = P_local*((1+(gamma/(gamma-1))*(M_inf**2))**(gamma/(gamma-1)))
    return P_localstag
    
def calc_P_localstag_super(P_infstag, M_inf):
    factor1 = ((gamma+1)*(M_inf**2)/2)/(1+((gamma-1)/2)*(M_inf**2))
    factor2 = (2*gamma/(gamma+1))*(M_inf**2) - ((gamma-1)/(gamma+1))
    P_localstag = P_infstag*(factor1**(gamma/(gamma-1)))*(factor2**(1/(1-gamma)))
    return P_localstag

def calc_mach_local(P_localstag, P_local):
    factor1 = (gamma-1)/gamma
    factor2 = ((P_localstag/P_local)**factor1)-1
    mach_local=(factor2*(2/gamma-1))**.5
    return mach_local

def calc_T_localstag(T_static, mach):
    T_localstag = T_static*(1+((mach**2)*(gamma-1)/2))
    return T_localstag

def calc_T_local(T_localstag, mach_local):
    T_local = T_localstag/(1+((gamma-1)/2)*mach_local**2)
    return T_local

def calc_T_recov(T_local, recov_fact, mach_local):
    T_recov = T_local*(1+(mach_local**2)*recov_fact*(gamma-1)/2)
    return T_recov

def calc_T_ref(T_local, T_recov,T_wall):
    T_ref=T_local+0.5*(T_wall-T_local)+0.22*(T_recov-T_local)
    return T_ref

def calc_k_ref(T_ref):      # NOTE: INCOMPLETE
    return 0.03

def calc_h(Nu, k_ref, dist):
    h=(3**0.5)*(Nu*k_ref)/dist
    return h

def calc_speed(mach, T):
    # Calculated using: https://www.grc.nasa.gov/www/k-12/airplane/sound.html
    R = 286                 # Gas constant
    c = np.sqrt(gamma*R*T)  # Speed of sound
    speed = mach*c
    return speed

def calcTemp(h, area, T_recov, T_wall, T_radref, mass, emmisivity, c_p, dt):
    print("h: ", h)
    print("T_recov: ", T_recov)
    print("T_wall: ", T_wall)
    print("T_radref: ", T_radref)
    temp = (((h*area*(T_recov-T_wall))-((5.67*(10**(-8)))*emmisivity*((T_wall**4)-(T_radref**4))))*dt/(mass*c_p))
    conv = (h*area*(T_recov-T_wall))*dt/(mass*c_p)
    rad = ((5.67*(10**(-8)))*emmisivity*((T_wall**4)-(T_radref**4)))*dt/(mass*c_p)
    print("conv: ", conv)
    print("rad: ", rad)
    print("temp: ", temp)
    T_wall_new = (((h*area*(T_recov-T_wall))-((5.67*(10**(-8)))*emmisivity*((T_wall**4)-(T_radref**4))))*dt/(mass*c_p))+T_wall
    return T_wall_new