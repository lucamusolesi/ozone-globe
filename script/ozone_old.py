import sys
from math import *
# Open Ozone data file and make a list of lines
ozfile = open('ozone.txt', 'r')
oz = ozfile.readlines()
ozfile.close()


# Delete information lines
del oz[0:3]

lon = [x / 10.0 for x in range(-1795,1805, 10)]
lat = [x / 10.0 for x in range(-895,905, 10)]


# Latitude list for the output
lati = []
for k in lat:
	for i in range(0,len(lon)):
		lati.append(k)

# Longitude list for the output
longi = lon*len(lat)


# List of O3 values in Dobson Units
DU = []

# Populate DU array
for ll in range(0,2700):
    for k in range(1,73+3,3):
    	    if k==31 and ((ll+1)%15==0): 
    	     	break                    	
            else: 
            	DU.append(oz[ll][k:k+3])


sys.stdout = open('ozone_b.json', 'w')

print "[[ 'giorno', ["
for j in range(0, len(DU)-1):
	print lati[j], ',', longi[j], ',', (int(DU[j])/100.)**(int(DU[j])/100.)/1000., ','
print lati[len(DU)-1], ',', longi[len(DU)-1], ',', (int(DU[len(DU)-1])/100.)**(int(DU[len(DU)-1])/100.)/1000.
print "]]]"

##print "[[ 'giorno', ["
##for j in range(0, len(DU)-1):
##	print lati[j], ',', longi[j], ',', exp(int(DU[j])/100.)/1000., ','
##print lati[len(DU)-1], ',', longi[len(DU)-1], ',', exp(int(DU[len(DU)-1])/100.)/1000.
##print "]]]"

# output=open("prova", "w")

# print>>output, "[[ 'giorno', ["
# for j in range(0, len(DU)):
# 	print>>output, lati[j], ',', longi[j], ',', DU[j], ','

# print>>output, lati[len(DU)-1], ',', longi[len(DU)-1], ',', DU[len(DU)-1]
# print>>output, "]]]"


