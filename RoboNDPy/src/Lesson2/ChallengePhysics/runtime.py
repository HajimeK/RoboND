#TODO: Write the python functions for the shown usages. 
#The functions are in the file called utils.py
#Use the above graph as a reference as you complete this 
#quiz

#Note: the program will not compile or execute
#error-free until the utils.py file is completed. 

import utils

startLocation = (0,0)
distanceX = 5
distanceY = 8
time = 1

newLocationX = utils.moveForwardX(distanceX, startLocation)
utils.printLocation(newLocationX)
    
newLocationY = utils.moveForwardY(distanceY, newLocationX)
utils.printLocation(newLocationY)

distance = utils.calcDistance(distanceX, distanceY)
print("distance = %f" %distance)

#time is in seconds, distance is in feet
velocity = utils.robotVelocity(distance, time)
print("velocity = %f" %velocity)
