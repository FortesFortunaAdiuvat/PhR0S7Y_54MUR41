import sys

# import math

# CONSTANTS
DEBUG = True
G = 3, 711


# MAX_VSPEED_LANDING = 40
# MAX_HSPEED_LANDING = 20
# MAX_POWER = 4
# MAX_ANGLE = 90

# DEBUG
def debug(*args):
    if (DEBUG):
        print(*args, file=sys.stderr, flush=True)


# INPUTS
def collect_land_data():
    land_values = []
    n = int(input())  # the number surfaceN of points forming the ground of Mars
    for i in range(n):
        land_x, land_y = [int(j) for j in
                          input().split()]  # pair of integers landX landY giving the coordinates of a point on the ground
        land_values.append([land_x, land_y])
    return land_values


def collect_capsule_data():
    return [int(i) for i in
            input().split()]  # single line consisting of 7 integers : X Y hSpeed vSpeed fuel rotate power


# GENERAL METHODS
def find_landing_zone(land_values):
    x1 = x2 = y = 0
    for x in land_values:
        if y == x[1]:
            x2 = x[0]
            break
        x1 = x[0]
        y = x[1]
    return [x1, x2, y]


def get_middle_x_landing_zone(landing_zone):
    mid_x = int((landing_zone[0] + landing_zone[1]) / 2)
    return mid_x


# CODE
landing_zone = find_landing_zone(collect_land_data())

middle_x_landing_zone = get_middle_x_landing_zone(landing_zone)

x1_landing_zone, x2_landing_zone, y_landing_zone = landing_zone

# CLASSES

# class Pod :

#     def __init__(self):
#         pass

#     def right_of_landing_zone(self):
#         pass

#     def left_of_landing_zone(self):
#         pass

#     def on_landing_zone(self):
#         pass


# GAME LOOP
while True:
    # X,Y are the coordinates in meters of the capsule.
    # hSpeed ​​and vSpeed ​​are respectively the horizontal speed and the vertical speed of Mars Lander (in m/s).
    # Depending on the movement of Mars Lander, the velocities can be negative.
    # fuel is the amount of remaining fuel in liters. When fuel runs out, rocket power drops too zero
    # rotate is the Mars Lander rotation angle in degrees.
    # power is the power of the capsule's rockets.
    x, y, hs, vs, f, r, p = collect_capsule_data()

    h = y - y_landing_zone  # height above the landing zone

    debug(h)

    P = R = 0

    #The capsule is on the left of the track
    if x < x1_landing_zone - 1000:
        # if it goes too fast
        if hs > 80:
            R = 10
            P = 4
        else:
            R = -45  #turn to the right
            P = 4

    # the capsule is on the left of the track but is approaching
    elif x < x1_landing_zone and x > x1_landing_zone - 1000:
        if hs < -90:
            R = -90
        elif hs > 90:
            R = 90
        else:
            R = hs
        P = 4



    # The capsule is on the right of the runway
    elif x > x2_landing_zone + 1000:

        # debug(y_landing_zone)
        # for the HIGH PLATEAU case
        if y_landing_zone > 2000:
            R = 0
            P = 4
        else:

            if hs < -80:
                R = -10
                P = 4
            else:
                R = +45  # turn to the left
                P = 4


    # the capsule is on the right of the runway but is approaching
    elif x > x2_landing_zone and x < x2_landing_zone + 1000:
        if hs < -90:
            R = -90
        elif hs > 90:
            R = 90
        else:
            R = hs
        P = 3

    # The capsule is on the landing strip
    elif x1_landing_zone < x < x2_landing_zone:

        # if we are close to the ground, we straighten the ship
        if h < 300:
            R = 0
            P = 4
        else:
            # perfect case
            if hs < 20 and hs > -20 and vs > -25:
                debug("perfect case")
                R = 0
                P = 3
            else:
                if hs < -90:
                    R = -90
                elif hs > 90:
                    R = 90
                else:
                    R = hs
                P = 4

    # R P. R is the desired rotation angle. P is the desired thrust power.
    print(R, P)
