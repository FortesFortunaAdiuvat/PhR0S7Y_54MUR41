import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# Bronze Level Code
lap_count = 1 # There are always 3 laps
min_boost_distance = 1000
boost_available = True
pod_force_field_radius = 400
checkpoint_radius = 600
map_width = 16000
map_height = 9000 # coordinate x=0 and y=0 is the top left pixel

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    thrust = 100
    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        thrust = 0
    # elif next_checkpoint_angle > 65 or next_checkpoint_angle < -65:
    #     thrust = 90
    elif (next_checkpoint_angle < 45 or next_checkpoint_angle > -45) and next_checkpoint_dist > min_boost_distance and boost_available:
        thrust = "BOOST"
    else:
        thrust = 100

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))
