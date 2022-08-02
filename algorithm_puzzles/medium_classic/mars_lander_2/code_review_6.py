import sys
import math

target_x1, target_y1, target_x2, target_y2 = 0, 0, 0, 0
last_x, last_y = 0, 0
surface_n = int(input())
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
    if last_y == land_y:
        target_x1 = last_x
        target_y1 = last_y
        target_x2 = land_x
        target_y2 = land_y
    last_x = land_x
    last_y = land_y

# game

stage = 1
approach_from = ""
counter = 0

while True:
    counter += 1
    x, y, h_speed, v_speed, fule, rotate, power = [
        int(i) for i in input().split()]
    if v_speed > 0:
        v_speed *= -1

    if h_speed != 0 and v_speed != 0:
        aoa = math.atan2(v_speed, h_speed)
        y0 = y - target_y1
        vector_mag = math.hypot(h_speed, v_speed)
        theta = aoa
        g = 3.711
        distance = (
            (vector_mag ** 2 / 2 * g)
            * (1 + (1 + (2 * g * y0 / (vector_mag ** 2 * math.sin(theta) ** 2))) ** 0.5)
        ) * math.sin(2 * theta)
        distance = (int(distance)/9)*-1
    angle = 0

    # First Stage

    if stage == 1:
        thrust = 4
        if x < target_x1:
            approach_from = "left"
            angle = -50
            if abs(h_speed) > 40:
                stage = 2
        elif x > target_x2:
            approach_from = "right"
            angle = 50
            if abs(h_speed) > 40:
                stage = 2
    elif stage == 2:
        angle = 0
        if counter % 7 == 0:
            thrust = 1
        else:
            thrust = 4
        comp_dist = int((distance * 0.2) * abs(h_speed * 0.01))
        if approach_from == "left" and comp_dist + x > target_x1:
            stage = 3
        if approach_from == "right" and comp_dist + x < target_x2:
            stage = 3
    elif stage == 3:  # SLOW DOWN
        thrust = 1
        opp_aoa = int((math.degrees(aoa) - 90) % 360 - 180)
        if opp_aoa >= 90:
            opp_aoa = 90
        if opp_aoa <= -90:
            opp_aoa = -90

        if abs(h_speed) > 1:
            if h_speed != 1:
                angle = opp_aoa
                thrust = 4
        else:
            angle = 0
            stage = 4
    elif stage == 4:  # LANDING
        if abs(v_speed) >= 40:
            thrust = 4
        else:
            thrust = 1

    print(str(angle) + " " + str(thrust))  # OUTPUT
