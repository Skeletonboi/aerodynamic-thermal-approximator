import math as m
from flightData import getAOA
from constants import *

gamma = get_gamma()

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
    factor2 = (P_localstag/P_local)**factor1-1
    mach_local=(factor2*(2/gamma-1))**.5
    return mach_local

def calc_T_local(T_localstag, mach_local):    
    T_local = T_localstag/(1+((gamma-1)/2)*mach_local**2)
    return T_local

def calc_T_recov(T_local, recov_fact, mach_local):
    T_recov = T_local*(1+(mach_local**2)*recov_fact*(gamma-1)/2)
    return T_recov

def calc_T_ref(T_local, T_recov):
    pass

def calc_k_ref(T_ref):
    pass

def calc_h(Nu, k_ref, dist):
    h=(3**0.5)*(Nu*k_ref)/dist
    return h

# Recursive function
'''
def calcTemp():     # Need to add arguments to this
    h2 = calc_h()   # Won't this always be equal to h1??
    while (abs(h2 - h1) >= 0.001):
        return
    pass
'''
