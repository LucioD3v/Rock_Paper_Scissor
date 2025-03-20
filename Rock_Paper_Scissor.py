'''
Create a Rock Paper Scissors game in Python. 
The game should randomly select a choice (Rock, Paper, Scissors) and then ask the user for their choice. 
The game should then determine the winner. 
Add a score counter that keeps track of the user's wins and losses.
'''

import random

# Define the choices
choices = ['rock', 'paper', 'scissors']

# Initialize the scores
user_score = 0
comp_score = 0

# Game loop
while True:
    # Get the computer's choice
    comp_choice = random.choice(choices)
    
    # Get the user's choice
    user_choice = input('Enter your choice (rock, paper, or scissors): ').lower()
    
    # Check for a draw
    if user_choice == comp_choice:
        print('It\'s a draw!')
    # Check for a user win
    elif user_choice == 'rock' and comp_choice == 'scissors':
        print('You win!')
        user_score += 1
    elif user_choice == 'paper' and comp_choice == 'rock':
        print('You win!')
        user_score += 1
    elif user_choice == 'scissors' and comp_choice == 'paper':
        print('You win!')
        user_score += 1
    # Check for a computer win
    elif user_choice == 'rock' and comp_choice == 'paper':
        print('You lose!')
        comp_score += 1
    elif user_choice == 'paper' and comp_choice == 'scissors':
        print('You lose!')
        comp_score += 1
    elif user_choice == 'scissors' and comp_choice == 'rock':
        print('You lose!')
        comp_score += 1
    # Check for invalid input
    else:
        print('Invalid input. Please try again.')
        continue
    
    # Display the scores
    print(f'Scores: You {user_score} - {comp_score} Computer')
    
    # Ask if the user wants to play again
    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again != 'yes':
        break
print('Thanks for playing!')