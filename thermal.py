from math import sqrt, cos



# Heat transfer within boundary layer as a func. of Mach#,
# altitude, and angle of attack. Laminar + Turbulent
# Based on the "Reference Temperature Method of Eckert" where
# heat transfer rates are calculated using incompressible flow
# eqns evaluated at Eckert's reference temp (between wall and
# recovery temp)
# Lumped heat capacitance method is used for thermally thin
# walls.
# Modified Mangler transformation is used for flow passing
# on conical side of vehicle, rest is flat plate.
# Heat transfer coefficient is calculated iterativelyy until
# at each time-step.

constant = {
"delta":5, # Wall Thickness
"k":6       # Heat Transfer Coefficient
}
# Biot Number Check (for thin wall)

# Recovery Temperature Subsonic
Cpmax = (PoL-Pinf)/q
PL = q*Cpmax*(cos(aoa)**2)+Pinf # [FIX] current cos is in radians
PoL = PL*((1+((gamma-1)/2)*(Minf**2))**(gamma/(gamma-1)))
# Recovery Temperature Supersonic
Poinf = Pinf*((1+((gamma-1/2))*(Minf**2))**(gamma/(gamma-1)))
t1 = ((gamma+1)*(Minf**2)/2)/(1+((gamma-1)/2)*(Minf**2))
t2 = (2*gamma/(gamma+1))*(Minf**2) - ((gamma-1)/(gamma+1))
PoL = Poinf*(t1**(gamma/(gamma-1)))*(t2**(1/(1-gamma)))
Ml = sqrt((((PoL/PL)**((gamma-1)/gamma))-1)*(2/(gamma-1)))
Tr = Tl*(1+r*((gamma-1)/2)*(Ml**2))