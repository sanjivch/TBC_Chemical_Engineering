# Ex. 8.4-1 Heat transfer area in Single-effect evaporator

F = 9072. # Salt solution entering in kg/h 
xF = 0.01 # solids concentration in Feed
xL = 0.015 # solids concentraton in exiting liquid
xV = 0.  # solids concentration in vapor is 0 as it is pure water vapor

cpF = 4.14 # Heat capacity of feed in kJ/kg.K
lat_heat = 2230. # Latent heat of steam at 143.3 kPa in kJ/ kg 
U = 1704. # Overall heat transfer coefficient in W/m**2.K

# Overall Mass balance, F = L + V 
# Component balance on solids, F*xF = L*xL + V*xV, on rearranging 

L = F*xF/xL

V = F - L  #From Overall mass balance

print "Liquid, L = %.4f kg/h \nVapor, V = %.4f kg/h"%(L,V)


