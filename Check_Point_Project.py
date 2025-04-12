import random

# Game intro
print('=========================')
print('Rock Paper Sissors')
print('=========================')
print('1) Rock')
print('2) Paper')
print('3) Scissors')

# Get user input
player = int(input('Choose your weapon (1-3): '))

# Generate computer's choice
computer = random.randint(1, 3)

# Map the choices
choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

print(f'You chose {choices[player]}')
print(f'Computer chose {choices[computer]}')

# Find out winner

if player == computer:
    print('Draw!')
elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
    print('Player - You win!')
else:
    print('Computer - You win!')
