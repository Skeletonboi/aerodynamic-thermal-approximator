# Lookup table for atmospheric properties (for altitude)
from constants import getGamma
from flightData import getSpeed

class Atmos:
	def __init__(self):
		# Viscosity and Density Tables (US American Toolbox)
		self.alt = [-1,0,1,2,3,4,5,6,7,8,9,10,15,20,25,30,40,50,60,70,80] # km
		self.nu = [1.821,1.789,1.758,1.726,1.694,1.661,1.628,1.595,1.561,1.527,1.493,1.458,1.422,1.422,1.448,1.475,1.601,1.704,1.584,1.438,1.321]
		self.rho = [1.347,1.225,1.112,1.007,0.9093,0.8194,0.7364,0.6601,0.5900,0.5258,0.4671,0.4135,0.1948,0.08891,0.04008,0.01841,0.003996,0.001027,0.0003097,0.00008283,0.00001846]
		self.temp_static=[294.65,288.15,281.65,275.15,268.66,262.17,255.68,249.19,242.70,236.21,229.73,223.25,216.65,221.55,226.51,250.35,270.65,247.02,219.58]

	def getNu(self,alt):
		# Assuming alt is given in meters
		alt = alt/1000
		idx = 0
		# Index to the correct altitude range
		while abs(alt-self.alt[idx]) < abs(alt-self.alt[idx + 1]):
			idx += 1
		# Interpolate between the altitude values
		diff = abs(alt - self.alt[idx])/(self.alt[idx+1]-self.alt[idx])
		# Return viscosity
		nu = self.nu[idx]+diff*abs(self.nu[idx]-self.nu[idx+1])
		return nu

	def getRho(self, alt):
		# Assuming alt is given in meters
		alt = alt / 1000
		idx = 0
		# Index to the correct altitude range
		while abs(alt - self.alt[idx]) < abs(alt - self.alt[idx + 1]):
			idx += 1
		# Interpolate between the altitude values
		diff = abs(alt - self.alt[idx]) / (self.alt[idx + 1] - self.alt[idx])
		# Return air density
		rho = self.rho[idx] + diff * abs(self.rho[idx] - self.rho[idx + 1])
		return rho

	def getT_static(self, alt):	#TODO: Add static temp data wrt altitude and extrapolate from that for this fnc
		# Assuming alt is given in meters
		alt = alt / 1000
		idx = 0
		# Index to the correct altitude range
		while abs(alt - self.alt[idx]) < abs(alt - self.alt[idx + 1]):
			idx += 1
		# Interpolate between the altitude values
		diff = abs(alt - self.alt[idx]) / (self.alt[idx + 1] - self.alt[idx])
		# Return viscosity
		T_static = self.temp_static[idx] + diff * abs(self.temp_static[idx] - self.temp_static[idx + 1])
		return T_static

	def getT_localstag(self, alt, speed, c_p):
		#https://en.wikipedia.org/wiki/Stagnation_temperature
		T_static = self.getT_static(alt)
		T_localstag = T_static + speed**2/(c_p*2)
		return T_localstag

if __name__=='__main__':
	x = Atmos()
	print(len(x.alt))
	print(len(x.nu))
	print(len(x.rho))