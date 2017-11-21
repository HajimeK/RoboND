#Write a python function for the following declarations:

import math

#all locations are tuples, which represent an x-y 
#coordinate pair.

#do not alter the printLocation function
def printLocation(location):
    print("Location = (%i, %i)" %(location[0],location[1]))   
    
def moveForwardX(distance, startLocation):
    #TODO: Calculate the distance along the
    #X (horizontal) axis. 
    #Return the new location as a tuple of 
    #coordinates x and y
    new = (startLocation[0] + distance, startLocation[1])
    return new

def moveForwardY(distance, startLocation):
    #TODO: Calculate the distance along the
    #Y (vertical) axis. 
    #Return the new location as a tuple of 
    #coordinates x and y
    new = (startLocation[0], startLocation[1] + distance)
    return new

def calcDistance(distanceX, distanceY):
    #TODO: Return the straight line distance
    #From the start location to the end location
    #Recall: x*x*x = x**3 in python
    return math.sqrt((distanceX * distanceX) + (distanceY * distanceY))
    

def robotVelocity(distance, time):
    #TODO: Return velocity using the straight line
    #distance and the given time
    return distance/time
