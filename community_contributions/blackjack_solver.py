import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

bank_cards = input().split(' ')
player_cards = input().split(' ')

number_cards = [2,3,4,5,6,7,8,9,10]
face_cards = ['J','Q','K']

player_hand_points = 0
house_hand_points = 0
player_hand_count = 0
house_hand_count = 0
for i in player_cards:
    print(i)
    player_hand_count += 1
    if i in number_cards:
        player_hand_points += i
    if i in face_cards:
        player_hand_points += 10
    if i == 'A' and player_hand_points < 21:
        player_hand_points += 11
    elif i == 'A' and player_hand_points >= 21:
        player_hand_points += 1

for i in bank_cards:
    house_hand_count += 1
    if i in number_cards:
        house_hand_points += i
    if i in face_cards:
        house_hand_points += 10
    if i == 'A' and house_hand_points < 21:
        house_hand_points += 11
    elif i == 'A' and house_hand_points >= 21:
        house_hand_points += 1

print(player_hand_count)
print(player_hand_points)

if house_hand_count == 2 and house_hand_points == 21:
    print('Bank')
elif player_hand_count == 2 and player_hand_points == 21 and player_hand_points > house_hand_points:
    print('Blackjack!')
elif player_hand_points > house_hand_points:
    print('Player')
elif player_hand_points == house_hand_points:
    print('Draw')
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


