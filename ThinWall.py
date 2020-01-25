def temp_calc(temp,dt,h,A,Tr,Tref,epsilon,mass,cp):
    sigma = 5.67 * 10 ** (-8)
    temp = (h*A*(Tr-temp)-sigma*epsilon*(temp**4-Tref**4))*dt/(mass*cp)+temp
    return temp