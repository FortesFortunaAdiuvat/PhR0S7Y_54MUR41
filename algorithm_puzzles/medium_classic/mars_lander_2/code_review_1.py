import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
list_surface=[]
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    list_surface.append([land_x,land_y])

for i in range(surface_n):
    if list_surface[i][1]==list_surface[i+1][1]:
        xlim1=list_surface[i][0]
        xlim2=list_surface[i+1][0]
        ylim=list_surface[i][1]
        break

stable=0
inzone=0
# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    #If we are far away from the zone
    if xlim1-x>500:
        if abs(h_speed)<50:
            print ("-30 4")
        elif abs(h_speed)>60:
            print("45 4")
        elif v_speed<0:
            print("0 4")
        elif v_speed>=0:
            print("0 3")
    
    if x-xlim2>500:
        if abs(h_speed)<50:
            print ("30 4")
        elif abs(h_speed)>60:
            print("-45 4")
        elif v_speed<0:
            print("0 4")
        elif v_speed>=0:
            print("0 3")
    
    #If we are close to the zone
    if xlim1-x<=500 and xlim1-x>=0:
        if inzone==0:
            print("45 4")
        else:
            print("-10 4")
    if x-xlim2<=500 and x-xlim2>=0:
        if inzone==0:
            print("-45 4")
        else:
            print("10 4")
    
    #If we are in the zone
    if x<xlim2 and x>xlim1:
        inzone=1
        print("Ici", file=sys.stderr)
        if stable==0: 
            if abs(h_speed)>10:
                print(str(int(45*math.floor(h_speed/abs(h_speed))))+" 4")
            elif abs(h_speed)>60:
                print(str(int(60*math.floor(h_speed/abs(h_speed))))+" 4")
            else:
                stable=1
                print("0 4")
        else:
            if v_speed<-39:
                
                print("0 4")
            else:
                print("0 3")
                
            