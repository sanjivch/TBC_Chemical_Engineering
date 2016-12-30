# Ex. 8.4-1 Heat transfer area in Single-effect evaporator

F = 9072. # Salt solution entering in kg/h 
xF = 0.01 # solids concentration in Feed
xL = 0.015 # solids concentraton in exiting liquid
xV = 0.  # solids concentration in vapor is 0 as it is pure water vapor

cpF = 4.14 # Heat capacity of feed in kJ/kg.K
hL = 0. # 
hV = 2257. #

Tf = 311. # in K 
T = 373.2 # in K
Ts = 383.2 # in K
lat_heat = 2230. # Latent heat of steam at 143.3 kPa in kJ/ kg 
U = 1704. # Overall heat transfer coefficient in W/m**2.K

# Overall Mass balance, F = L + V 
# Component balance on solids, F*xF = L*xL + V*xV, on rearranging 

L = F*xF/xL

V = F - L  #From Overall mass balance

S = (-F*cpF*(Tf-T)+L*hL+V*hV)/lat_heat

A = (S*lat_heat/(U*(Ts-T)))*(1000./3600)

print "Liquid, L = %.4f kg/h \nVapor, V = %.4f kg/h \nSaturated steam, S = %.4f kg/h \nArea, A = %.4f m**2"%(L,V,S,A)

#===========================================================================================

