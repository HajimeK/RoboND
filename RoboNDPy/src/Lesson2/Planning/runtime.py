#Use the Robot class in util.py.
#Write code that will move the robot 
#on one of the two paths listed above. 

#Note: the program will not compile or execute
#error-free until the utils.py is completed. 

import utils

startLocation=(0,0,'S')

r1 = utils.Robot(startLocation)
loc1 = r1.rotate(startLocation, 'N')
loc2 = r1.moveForward(loc1,5)
loc3 = r1.rotate(loc2, 'E')
endLocation = r1.moveForward(loc3,15)

#endLocation should be (15,5,E)

print endLocation