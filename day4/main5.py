import random

#rock, paper, scissors

#rps rules ->
# rock beats scissors
# paper beats rock
# scissors beats paper


rps = ['rock', 'paper', 'scissors']

#computers choice
computers_choice = random.choice(rps)

#players choice
rps_indx = int(input(('rock -> 0. paper -> 1, scissors -> 2 ')))
players_choice = rps[rps_indx]

print(f'You played {players_choice} & computer played {computers_choice}')

if computers_choice == players_choice:
    print('Issa Tie')

#player plays rock
if players_choice == rps[0]:
    if computers_choice == rps[1]:
        print('You Lost')
    else:
        print('You Win')

#player plays paper
if players_choice == rps[1]:
    if computers_choice == rps[2]:
        print('You Lost')
    else:
        print('You Win')

#player plays scissors
if players_choice == rps[2]:
    if computers_choice == rps[1]:
        print('You Lost')
    else:
        print('You Win')