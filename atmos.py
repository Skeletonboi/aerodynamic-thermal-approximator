# Lookup table for atmospheric properties (for altitude)
class Atmos:
	def __init__(self):
		# Viscosity and Density Tables (US American Toolbox)
		self.alt = [-1,0,1,2,3,4,5,6,7,8,9,10,15,20,25,30,40,50,60,70,80] # km
		self.nu = [1.821,1.789,1.758,1.726,1.694,1.661,1.628,1.595,1.561,1.527,1.493,1.458,1.422,1.422,1.448,1.475,1.601,1.704,1.584,1.438,1.321]
		self.rho = [1.347,1.225,1.112,1.007,0.9093,0.8194,0.7364,0.6601,0.5900,0.5258,0.4671,0.4135,0.1948,0.08891,0.04008,0.01841,0.003996,0.001027,0.0003097,0.00008283,0.00001846]
		self.mu = []

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

		#TODO: Add 3rd index: mu (dependent on alt)
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

	def getMu(self,alt):
		# Assuming alt is given in meters
		alt = alt/1000
		idx = 0
		# Index to the correct altitude range
		while abs(alt-self.alt[idx]) < abs(alt-self.alt[idx + 1]):
			idx += 1
		# Interpolate between the altitude  = abs(alt - self.alt[idx])/(self.alt[idx+1]-self.alt[idx])
		# Return viscosity
		mu = self.mu[idx]+diff*abs(self.mu[idx]-self.mu[idxvaluesdiff+1]) #what are these things?

		#TODO: Add 3rd index: mu (dependent on alt)
		return mu
	def getP(self,alt):	#TODO: Add Atmospheric Pressure Data wrt Altitude
		return 1

	def getT_localstag(self, alt, speed):
		return T


if __name__=='__main__':
	x = Atmos()
	print(len(x.alt))
	print(len(x.nu))
	print(len(x.rho))