import sys
from math import *
import urllib2

# Download the needed file
dl= urllib2.urlopen('ftp://toms.gsfc.nasa.gov/pub/omi/data/ozone/Y2006/L3_ozone_omi_20060101.txt')


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
for ll in range(0,len(oz)):
    for k in range(1,73+3,3):
    	    if k==31 and ((ll+1)%15==0): 
    	     	break                    	
            else: 
            	DU.append(oz[ll][k:k+3])


#Another way to fill the DU list
# DU = []

# for index, line in enumerate(oz):
#    line = line.strip() if float(index +1) % 15 != 0 else line.strip().split(' ')[0]
#    for i in range(0,len(line)-3,3):
#       DU.append(line[i:i+3])



# out=open('out.json','w')
# out.write("[[\"giorno\",[")
# for j in range(0, len(DU)-1):
#         if int(DU[j])!=0:
#                 out.write(str(lati[j])+','+str(longi[j])+','+str((int(DU[j])/100.)**(int(DU[j])/100.)/1000.)+',')
# if DU[len(DU)-1]!=0:
#         out.write(str(lati[len(DU)-1])+','+str(longi[len(DU)-1])+','+str((int(DU[len(DU)-1])/100.)**(int(DU[len(DU)-1])/100.)/1000.))
# out.write("]]]")
# out.close()


#Output with value DU*DU without spaces or \n
out=open('out.json','w')
out.write("[[\"giorno\",[")
for j in range(0, len(DU)-1):
        if int(DU[j])!=0:
                out.write(str(lati[j])+','+str(longi[j])+','+"{0:.4f}".format((int(DU[j])/100.)**(int(DU[j])/100.)/1000.)+',')
if DU[len(DU)-1]!=0:
        out.write(str(lati[len(DU)-1])+','+str(longi[len(DU)-1])+','+"{0:.4f}".format((int(DU[len(DU)-1])/100.)**(int(DU[len(DU)-1])/100.)/1000.))
out.write("]]]")
out.close()



#Output with value DU*DU
sys.stdout = open('ozone_a.json', 'w')
print "[[ \"giorno\", ["
for j in range(0, len(DU)-1):
        if int(DU[j])!=0:
                print lati[j], ',', longi[j], ',', (int(DU[j])/100.)**(int(DU[j])/100.)/1000., ','
if DU[len(DU)-1]!=0:
        print lati[len(DU)-1], ',', longi[len(DU)-1], ',', (int(DU[len(DU)-1])/100.)**(int(DU[len(DU)-1])/100.)/1000.
print "]]]"


#Output with value exp(DU)
sys.stdout = open('ozone_exp.json', 'w')
print "[[ \"giorno\", ["
for j in range(0, len(DU)-1):
        if int(DU[j])!=0:
                print lati[j], ',', longi[j], ',', exp(int(DU[j])/100.)/1000., ','
if DU[len(DU)-1]!=0:
        print lati[len(DU)-1], ',', longi[len(DU)-1], ',', exp(int(DU[len(DU)-1])/100.)/1000.
print "]]]"

##sys.stdout = open('ozone.json', 'w')
##
##print "[[ \"giorno\", ["
##for j in range(0, len(DU)-1):
##	print lati[j], ',', longi[j], ',', DU[j], ','
##print lati[len(DU)-1], ',', longi[len(DU)-1], ',', DU[len(DU)-1]
##print "]]]"



