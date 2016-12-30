# Ex. 14.5-1 Power to crush Iron ore by Bond's Theory
import math

#Variables
dF = 3./12  # feed size in ft - converted from inches to feet
dP = (1./8)/12 # product size in ft

T = 10./60 # Feed rate in ton/ min - Converted from ton/h to ton/min
Ei = 12.68 # Work Index for Hematite

#Calculation
#From Eq. 14.5-6, the Bond's equation for English units is

P = 1.46*Ei*T*(dP**(-1./2)-dF**(-1./2))

#Results
print "Gross power required, P = %.4f hP"%P

#==============================================================================================
