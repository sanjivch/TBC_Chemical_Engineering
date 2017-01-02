# Ex. 1.5-2 Crystallization of KNO3 and Recycle

F = 1000 # Feed in kg/h 
xF = 0.2 # 20 wt% solids in Feed 
xR = 0.375 # wt% in recycle stream
xP = 0.96 # wt% in products stream 
xS = 0.5 # wt% in stream to crytsallizer 
xW = 0. # wt% in water is 0 
#Calculation

# Overall Mass balance, F = W + P
# Component mass balance on solids(KNO3) F*xF = W*xW + P*xP, rearranging,

P = F*xF/xP

# Mass balance around the crytsallizer, S = P + R,  
# Component balance on solids around crystallizer, S*xS = P*xP + R*xR, rearraning,

R = P*(xS-xP)/(xR-xS)

S = P + R

print "Product, P = %.4f kg/h \nRecycle, R = %.4f kg/h \nStream inlet to Crystallizer, S = %.4f kg/h "%(P, R, S)

#============================================================================================
# Ex. 1.5-3 Combustion of fuel gas 
#============================================================================================

# Ex. 1.6-2 Heating of milk 

m = 4536 # Mass flow in kg/h 
Cp = 3.85 # Heat Capacity in kJ/kg. K 
T1 = 4.4 # Inlet temperature in deg C 
T2 = 54.4 # Outlet temperature in deg C 

Q = m*Cp*(T2-T1)/3600.

print "Heat required, Q = %.4f kW "%Q

#=============================================================================================






