import sys
import math


power = 0
rotate = 0
sur_pins = []
y_points = []


surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    sur_pins.append([i, land_x, land_y])
    y_points.append(land_y)



tallest_point = max(y_points)
flat_sur = []


#landing_spot = flat_sur[1][1] - flat_sur[0][1]



for index, element in enumerate(sur_pins):
        prev_pin = sur_pins[index-1]
        if (prev_pin[2] == element[2]):
            flat_sur.append(prev_pin)
            flat_sur.append(element)










# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]


    if (x < flat_sur[0][1]):
        if (h_speed > 30 and  tallest_point < y < 2800):
            power = 4
            rotate = 5

        elif (y < tallest_point and h_speed > 50):
            power = 4
            rotate = 15


        elif (y < tallest_point):
            power = 4
            rotate = -15
        


        elif (h_speed > 30):
            power = 4
            rotate = 40

        else:
            power = 4
            rotate = -40



    elif (flat_sur[1][1] < x):
        if (h_speed < -30 and  tallest_point < y < 2800):
            power = 4
            rotate = -5
            
        elif (y < tallest_point and h_speed > 0):
            power = 4
            rotate = 90


        elif (y < tallest_point):
            power = 4
            rotate = -15
        


        elif (h_speed < -30):
            power = 4
            rotate = -90


        else:
            power = 3
            rotate = 60


    elif (x >= flat_sur[0][1] and x <= flat_sur[1][1]):
        if (v_speed > -39 and -15 < h_speed < 15): 
            power = 3
            rotate = 0

        elif (20 < h_speed):
            power = 4
            rotate = 45 
        

        elif (-20 > h_speed):
            power = 4
            rotate = -45 

        elif (v_speed < -39): 
            power = 4
            rotate = 0
        
        else: 
            power = 3
            rotate = 0
        



    print(rotate, power)


    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.

