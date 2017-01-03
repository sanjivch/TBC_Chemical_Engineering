
#=============================================================================================
# Ex. 2.2-1 Units and dimensions of Force 

m = 3 # mass in lbm 

# Part (a) - Lb force  
g = 32.174 # acceleration due to gravity, ft/s**2 
gc = 32.174 # gravitaion conversion factor, lbm.ft/lbf.s**2 

F = m*g/gc

print "Force = %.1f lbf"%F 

# Part (b) - Dynes
m = 3*453.59 # mass is converted from lb to g
g = 980.665 # acceleration due to gravity, cm/s**2 

F = m*g # Force in Dynes

print "Force = %.3e Dynes"%F

# Part (c) - Newtons
m = 3*.45359 # mass is converted from lb to kg
g = 9.80665 # acceleration due to gravity, m/s**2 

F = m*g # Force in Newtons 

print "Force = %.2f Newtons"%F

#=============================================================================================
# Ex. 2.2-2 Pressure in Storage Tank
# SI units
P0 = 101325. # Pa 
h1 = 3.05 # m 
h2 = 0.61 # m 
rho1 = 917 # kg/m**3 
rho2 = 1000 # kg/m**3 
g = 9.8066 # m/s**2

P1 = P0 + (rho1*g*h1)
P2 = P0 + (rho1*g*h1) + (rho2*g*h2)
Pgage = P2-P0

print "SI units: P1 = %.3e Pa \nP2 = %.3e Pa \nPgage = %.3e Pag"%(P1,P2,Pgage)

# English units
P0 = 14.696 # psi 
h1 = 10. # ft   
h2 = 2. #  ft  
rho1 = 0.917*62.43 # convert g/cm**3 to lb/ft**3 
rho2 = 1*62.43 # convert g/cm**3 to lb/ft**3 
g = 32.174 # convert ft/s**2 to in/s**2
gc = 32.174 

P1 = P0 + (rho1*g/gc*h1)/144.
P2 = P0 + ((rho1*g/gc*h1) + (rho2*g/gc*h2))/144.
Pgage = P2-P0

print "\nEnglish units: P1 = %.2f psi \nP2 = %.2f psi \nPgage = %.2f psig"%(P1,P2,Pgage)

#=========================================================================================
# Ex. 2.2-4 Pressure difference in a manometer

rhoA = 13.6 #g/cm**2
rhoB = 1 #g/cm**2 
R = 32.7 # cm 
g = 9.80665 # m/s**2 

deltaP = (R/100.)*(rhoA - rhoB)*(1000.)*g

print "Pressure difference = %.3e N/m**2"%deltaP

#=========================================================================================

#Ex. 2.2-5 Derivation
#=========================================================================================
