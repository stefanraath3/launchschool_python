import random

VALID_CHOICES = ['rock', 'paper', 'scissors']



def prompt(message):
    print(f"==> {message}")

def display_winner(player, computer):

    prompt(f'Your chose {player}, computer chose {computer}')


    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        prompt("You win!")

    elif ((player == "rock" and computer == "paper") or
        (player == "paper" and computer == "scissors") or
        (player == "scissors" and computer == "rock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

while True:
    # Ask the user to choose 
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt('That is not a valid choice')
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)
    display_winner(choice, computer_choice)
    

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while answer == '' or (answer[0] != 'n' and answer[0] != 'y'):
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] != "y":
        break

     
    