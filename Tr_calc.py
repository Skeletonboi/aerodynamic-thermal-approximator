import math
# Relevant variables
# Tr=recovery temperature
# Tl=local temperature
# T0L
# r=recovery factor
# gamma=specific heat flow ratio
# Ml=local mach number
# P0L=local stagnation pressure
# Pl=local pressure
# Minf=free stream mach number
# Cpmax=maximum pressure coefficient on the body surface
# q=dynamic presure
#Pr- prandtl number

#needed inputs
#T0L,gamma,isLaminar,Pr,Cpmax,AOA,Pinf,q,Minf


def get_Tr(T0L,gamma,isLaminar,Pr,Cpmax,AOA,Pinf,q,Minf):
	Ml=get_Ml(Cpmax,gamma,AOA,Pinf,q,Minf)
	Tl=T0L/(1+((gamma-1)/2)*Ml)
	if (isLaminar==True):
		r=sqrt(Pr)
	else:
		r=Pr**(1/3)
	Tr_cal=Tl*(1+(r*(gamma-1)/2)*(ML**2))
	return Tr_cal

def get_Ml(Cpmax,gamma,AOA,Pinf,q,Minf):
	Pl=q*Cpmax*(cos(AOA)**2)+Pinf
	P0L=Pl*(1+((gamma-1)/2)*(Minf**2))**(gamma/(gamma-1))
	Ml_cal=sqrt((((P0L/Pl)**((gamma-1)/gamma))-1)*(2/(gamma-1)))
	return Ml_cal