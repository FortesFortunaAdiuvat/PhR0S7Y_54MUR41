import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def d(msg):
    print(msg, file=sys.stderr, flush=True)


surface_n = int(input())  # the number of points used to draw the surface of Mars.

G = 3.711
maxHspeed = 20
maxVSpeed = 40

lastx = lasty = startx = endx = landingy = -1

#math.degrees()

for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    landx, landy = [int(j) for j in input().split()]

    if lasty == landy and startx == -1:
        startx = lastx
        landingy = landy
    elif startx != -1 and endx == -1:
        endx = lastx

    lastx = landx
    lasty = landy

while True:
    x, y, hSpeed, vSpeed, fuel, rotate, power = [int(i) for i in input().split()]
    speed = math.sqrt( math.pow(hSpeed,2) + math.pow(vSpeed, 2) )
    
    aimAngle = math.degrees(math.acos(G / 4))

    angle = 0
    acc = 4

    if not (startx <= x and x <= endx) :
        # if it is not over the target
        if (x < startx and hSpeed < 0) or (endx < x and hSpeed > 0) or abs(hSpeed) > 4 * maxHspeed:
            # if it goes in wrong direction or goes too fast horizontally
            angle = round(math.degrees(math.asin(hSpeed / speed))) # if angle is to slow
        elif abs(hSpeed) < 2 * maxHspeed:
            # if it goes too slow horizontally

            if x < startx:
                angle = -aimAngle
            elif end < x:
                angle = aimAngle
            else:
                angle = 0

            angle = round(angle)

        elif vSpeed >= 0 :
            acc = 3
    else:
        if y < 200 + landingy:
            # is finishing, i.e. Y is < critical height
            acc = 3
        elif (abs(hSpeed) <= maxHspeed - 5) and (abs(vSpeed) <= maxVSpeed - 5):
            # has safe speed
            acc = 2
        else:
            # if angle is to slow;
            angle = round(math.degrees(math.asin(hSpeed / speed)))

    print(angle, acc)