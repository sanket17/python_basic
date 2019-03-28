'''
Simple Python Game
Number guessing game


Algo:
1. Generate a random number between 1-100
2. Save the number in variable
3. Accept a 2 digit number from user.
4. Generated number and user inputed number difference
5. If difference is less then 10 print CLOSE and go to step 8
6. If difference is 0 then print MATCH and go to step 8
7. If difference is greater than 10 print NO MATCH and go to step 8
8. Ask user if he wish to play more.
9. If yes, then accept another number and goto step 4
10.If No, then print the generated number and display thank you message and exit.

'''
from __future__ import print_function
from random import randint

def generate_random_number():
    '''
     This function generates a random number to predict
     INPUT: No input
     OUTPUT: Random 2 digit number
    '''
    return randint(0, 99)

def accept_number_from_user():
    '''
     This function takes 2 digit number from user
     INPUT: No input
     OUTPUT: 2 digit number
    '''
    number = int(input('\nEnter two digit number: '))
    return number

def start_game():
    '''
     This function play's number guessing game
     INPUT: No input
     OUTPUT: Generated Number
    '''
    play = True
    generated_number = generate_random_number()
    while play:
        user_inputed_number = accept_number_from_user()
        if generated_number == user_inputed_number:
            print("MATCH")
            break
        elif abs(generated_number - user_inputed_number) <= 10:
            print("CLOSE")
        else:
            print("No match")
        choice = input('Do you want to guess again(y=yes|n=no): ')
        print(choice)
        if choice.lower() == "n":
            play = False
    return generated_number

def play_game():
    '''
     This function defines rules and regulation for the game.
     And gives opportunity to replay the game
     INPUT: No input
     OUTPUT: No output
    '''
    print('Welcome to NUMBER GUESSING game!!\nGuess Two digit number between 0-99\n')
    print('Rules:')
    print('Difference between actual number and your inputed number is caluculated')
    print('1. If difference is less than 10 message will be displayed as CLOSE')
    print('2. If match is found MATCH message is displayed.')
    print('3. If difference is more than 10, NO MATCH message is displayed')
    play_again = True
    number = 0

    while play_again:
        number = start_game()
        choice = input("\nDo you want to play again(y=yes/ n=no): ")
        if choice.lower() == 'n':
            play_again = False
    print('Generated Number was: {}'.format(number))
    print('Thank you for playing!!!')

play_game()
