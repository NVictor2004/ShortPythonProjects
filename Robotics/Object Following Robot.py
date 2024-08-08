
from martypy import Marty

robot = Marty("wifi", "192.168.137.197")

lmin = 768
lmax = 57089
rmin = 1
rmax = 149

maxdistance = 10
maxdistance = 1 / maxdistance
anglescale = 3
time = 1000

while True:
    ldis = robot.get_obstacle_sensor_reading("left") #get sensor values
    rdis = robot.get_obstacle_sensor_reading("right")
    
    ldis = (ldis - lmin) / lmax # normalise to between 0 and 1
    rdis = (rdis - rmin) / rmax

    # Convert to acceptable values
    ldis, rdis = 1 / (ldis + maxdistance), 1 / (rdis + maxdistance)

    print(ldis, rdis)

    angle = rdis - ldis
    
    robot.walk(1, "left", angle * anglescale, ldis, time)
    robot.walk(1, "right", angle * anglescale, rdis, time)

    

    


