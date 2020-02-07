# Contains calculations for all dimensionless numbers. Namely:
#     * Reynold's Number
#     * Prandlt's Number
#     * Nusslet Number

def calcRe (rho, mu, vel, x_cr):
    return rho*vel*x_cr/mu

def calcPr (mu, k, c_p):
    return c_p*mu/k

def calcNu (Re, Pr, isLaminar):
    if (isLaminar):
        return 0.33206*sqrt(Re)*(Pr**(1/3))
    else:
        return 0.02914*(Re**(0.8))*(Pr**(1/3))
