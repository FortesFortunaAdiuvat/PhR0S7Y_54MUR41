import sys
from math import radians, degrees, cos, sin, acos, asin, hypot

surface_n = int(input())
land_x1, land_y1 = -1, -1
for i in range(surface_n):
    land_x2, land_y2 = [int(j) for j in input().split()]
    if land_x2 - land_x1 >= 1000 and land_y2 == land_y1:
        target_left, target_right = land_x1, land_x2
        target_y = land_y2
    land_x1, land_y1 = land_x2, land_y2

max_speed = 60
g = 3.711 # m/s**2

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    angle = radians(90 - rotate)
    
    # target_y = -(1 / 2) * g * t ** 2 + (-v_speed) * t + y
    # v(t) = -g * t + (-v_speed)
    
    # g_x = cos(angle) * p
    # g_y = sin(angle) * p - g
    
    # landing
    if x > target_left and x < target_right and abs(h_speed) < 5:
        sec_2_stop = v_speed / (4 - g)
        height_at_stop = (1 / 2) * (4 - g) * sec_2_stop ** 2 - v_speed * sec_2_stop + y
        p = 4 if height_at_stop <= target_y else 0
        r = 0
        
    # moving horizontally
    else:
        p = 4
        if x < target_left:
            v_x = max_speed
        elif x > target_right:
            v_x = -max_speed
        else:
            v_x = 0
        v_y = 0
        direction = -1 if h_speed > v_x else 1
        cos_a = (v_x - h_speed) / p
        sin_a = (v_y - v_speed + g) / p
        angle = asin(sin_a / hypot(cos_a, sin_a))
        r = direction * round(degrees(angle) - 90)
        if abs(r) == 180:
            p = 0
            r = 0
        else:
            r = max(-90, min(90, r))
            
    print(r, p)
