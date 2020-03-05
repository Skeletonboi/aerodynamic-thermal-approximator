import math as m
from flightData import getAOA

def calc_P_local(C_pmax, P_inf, q, AOA):
    #q : dynamic pressure
    #C_pmax : maximum pressure coefficient on the body surface
    #P_inf : free stream pressure
    return q*C_pmax*(m.cos(AOA)**2)+P_inf

def calc_P_infstag(M_inf):


def calc_P_localstag_sub(P_local, P_infstag, M_inf):


def calc_P_localstag_super(P_infstag, M_inf):


def calc_mach_local(P_localstag, P_local):


def calc_T_local(T_localstag, mach_local):


def calc_T_recov(recov_fact, mach_local):


def calc_T_ref(T_local, T_recov):


def calc_k_ref(T_ref):


def calc_h(Nu, k_ref, dist):


def calcTemp():     # Need to add arguments to this
