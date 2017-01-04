
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
# Ex 2.2-3 Conversion of Pressure to head of a fluid

# Part (a)
# At T = 4 deg C, the density of water is 1.0 g/cm**3(= 1000 kg/m**3)
rho = 1000 # density of water in kg/m**3 
g = 9.80665 # acceleration due to gravity in m/s**2 
P = 101325 #  Pressure in N/m**2
#P = rho*g*Head, on rearranging, 
Head = P/(rho*g)
print "Head = %.4f m of water at 4 deg C"%Head

# Part (b)
# At T = 0 deg C, the density of Hg is 13.5955 g/cm**3(=13595.5 kg/m**3)
rho = 13595.5 # density of Hg in kg/m**3
g = 9.80665 # acceleration due to gravity in m/s**2 
P = 101325 #  Pressure in N/m**2
#P = rho*g*Head, on rearranging, 
Head = P/(rho*g)
print "Head = %.4f m of Hg"%Head
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
# Ex. 2.3-1 Molecular transport of a property at steadt state 

c1 = 1.37e-02 # concentration at position 1 in amount of property/m**3
c2 = 0.72e-02 # concentration at position 2 in amount of property/m**3
z1 = 0. # position 1 in m 
z2 = 0.4 # position 2 in m 
diffusivity = 0.013 # in m**2/s 
# Part (a)

Flux = diffusivity*(c1-c2)/(z2-z1) # From Eq. 2.3-4  

print "Flux = %.3e amount of property/s m**2"%Flux

# Part (b) - Derivation 

# Part (c)
z = (z1+z2)/2. # midpoint
#From Eq. 2.3-6
c = c1 + (Flux/diffusivity)*(z1-z)

print "Concentration at mid point of path = %.3e amount of property/m**3"%c
#========================================================================================================================

# Ex. 2.5-1 Reynolds number in a Pipe
# English units  
q = 10/(7.481*60) # convert gal/min to ft**3/s


D = 2.067/12. # convert in to ft
A = (3.14*D**2)/4. # in ft**2
v = q/A # in ft/s
rho = 0.996*62.43 # convert g/cm**3 into lbm/ft**3 
mu = 0.8007*6.7197e-04 # convert cp(g/cm s) to lbm/ft s   

Re = D*v*rho/mu 

print "Reynolds no. = %.3e"%Re

# SI units  
q = 10*3.785e-03/60 # convert gal/min to m**3/s


D = 2.067*0.0254 # convert in to m
A = (3.14*D**2)/4. # in m**2 
v = q/A # in m/s
rho = 0.996*1000. # convert g/cm**3 into kg/m**3 
mu = 0.8007*0.001 # convert cp(0.01 g/cm s) to kg/m s 

Re = D*v*rho/mu 

print "Reynolds no. = %.3e"%Re
