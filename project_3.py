# -*- coding: utf-8 -*-
"""
Created on Mon May 01 16:09:33 2017

@author: Libby
"""
import numpy as np
from matplotlib import pyplot as plt

##Global mean temperature as described by Walsh, et al, Oberlin College

##R(dT/dt) = Q(1-alpha)-(sigma*T^4)

##T -> Temperature in Kelvin, average temp in upper atmosphere.
##t -> Time, in years
##R -> (W-sec)/(m^2*K), average heat capacity of Earth/Atmosphere system
##Q -> (W/m^2), average annual solar radiation per square meter of Earth surface
##alpha ~ a -> dimensionless, planetary albedo
##sigma ~ s -> (W)/(m^2*(K^4)), Stefan-Boltzmann constant of proportionality

##Solve for Q, determine average annual solar radiation

R = 2.912*(3.15*10**7) #(W-sec)/((m^2)(K))
a = 0.30
s = 5.67*10**-8 #W/m^2K^4
Q = 324 #W/m^2
T = [300]
#t = (5, 10, 15, 20, 25, 30)
dt = 3600*24
t = np.arange(0, 1000*dt, dt)

##Using algebra, find T on one side of equation...

##h = (T_l+1 - T_l) / (del_T)
##R(h) = Q(1-a)-(s*T^4)
#T_l+1 = (( Q(1-a) - s*T^4)* (del_t/ R) + T_l)

#Loop T so the new Temperature is function of old Temperature
for ti in t:
    T.append( (Q*(1-a) - s*(T[-1]**4))*(dt/R) + T[-1] )
    
    #Print new T
    print T[-1]
    
    #Plot T vs t
    plt.plot(T)
    #add axis labels and title
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (K)')
    plt.title('Global Mean Temperature')
plt.plot()
plt.show()