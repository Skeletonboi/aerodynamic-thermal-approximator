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

data = []       # Each index contains: [altitude, h]

# Data entry
h = 0.001 # Global Variable
constant = {
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
bi = h*(constant.delta/constant.k)
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
        PoL = Poinf*(t1**(gamma/(gamma-1)))*(t2**(1/(1-gamma)))
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
print("Altitude\t\th")
for val in data:
    print(val[0] + "\t\t\t" + val[1])
