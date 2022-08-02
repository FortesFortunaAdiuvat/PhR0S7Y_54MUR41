import sys
import math

def get_distance_from_ground(x, y, surface):
    for i in range(len(surface) - 1):
        if surface[i][0] <= x <= surface[i + 1][0]:
            a = (surface[i+1][1] - surface[i][1])/(surface[i+1][0] - surface[i][0])
            b = surface[i][1] - a * surface[i][0]
            return y - int(a * x + b)

def get_distance_from_target(target, position):
    return math.sqrt(get_distance_vector(target, position)[0]**2 + get_distance_vector(target, position)[1]**2)
    
def get_distance_vector(target, position):
    return [target[0]-position[0], target[1]-position[1]]

def get_angle_from_target(target, position):
    return 180 * math.asin(get_distance_vector(target, position)[1] / get_distance_from_target(target, position)) / math.pi

def get_new_rotation(target, position, h_speed, dist_from_ground):
    a = get_angle_from_target(target, position)
    d = get_distance_from_target(target, position)
    print('angle from traget:   %.2f' % a, file=sys.stderr)
    print('distance from traget:%.2f' % d, file=sys.stderr)
    sign = 1 if x > target[0] else -1
    angle_max = 90
    if d > 1000 and abs(a) < 25:
        new_rot = h_speed/3 + sign * 180 * math.acos(3.711/4) / math.pi
    else:
        new_rot = 0
        if dist_from_ground >= 200:
            ratio = abs(target[0] -  position[0]) / target[0]
            new_rot = h_speed + sign * angle_max * ratio
    return max(-90, min(90, int(round(new_rot))))

def get_new_power(target, position, v_speed, h_speed, dist_from_ground):
    if position[1] < 2950 and v_speed < 2:
        new_pow = math.sqrt(int(-v_speed / 10) ** 2 + int(h_speed / 10) ** 2)
    else:
        new_pow = 2
    return max(0, min(4, int(round(new_pow))))

def get_target_coord(surface):
    for i in range(surface_n-1):
        if surface[i][1] == surface[i+1][1]:
            xmin, ymin = surface[i]
            xmax, ymax = surface[i+1]
    return [int(round((xmin + xmax) / 2)), ymin]

surface_n = int(input())  # the number of points used to draw the surface of Mars.
surface = dict()
for i in range(surface_n):
    surface[i] = [int(j) for j in input().split()]
target = get_target_coord(surface)

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    print('target: x-%s y-%s' % (target[0], target[1]), file=sys.stderr )
    dist = get_distance_from_ground(x, y, surface)
    print('distance from ground:', dist, file=sys.stderr)
    
    new_rot = get_new_rotation(target, [x, y], h_speed, dist)
    new_pow = get_new_power(target, [x, y],  v_speed, h_speed, dist)
    
    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print(new_rot, new_pow)
