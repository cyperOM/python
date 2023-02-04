
#Code by cyperom.me
#This will calculate the ditance between your current location and the nearest branch 
#Install geopy using  "pip install geopy"

import math
from geopy.geocoders import Nominatim
 
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")
 
# entering the location name
getLoc = loc.geocode("My location")
 
Mylocation = [getLoc.longitude,getLoc.latitude]
Branchs = [[50,80], [1,2],[90,70]] #longitude and latitude cords 
DISTANCE = []
#Calculate the distance between my location and the branches.

for r in Branchs:
    X=(Mylocation[0]-r[0])*(Mylocation[0]-r[0])
    Y=(Mylocation[1]-r[1])*(Mylocation[1]-r[1])
    Temp = math.sqrt(X+Y)
    DISTANCE.append(Temp)

DISTANCE.sort()
print(DISTANCE)
