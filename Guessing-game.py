import random as rd
computer_guess = rd.randint(1,51)

user_guess = int(input('Enter the guess number: '))
attempt = 1

while computer_guess != user_guess:
    if computer_guess < user_guess:
        print('Please guess lower number.')
    elif computer_guess > user_guess:
        print('Please guess higher number.')

    user_guess = int(input('Type the number again: '))
    attempt += 1
        
else:
    print('Cogratulations! you have won the match.')
    print('Your total attempt is',attempt)