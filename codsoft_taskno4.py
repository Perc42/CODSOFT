import random

def game():
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ")
        computer_choice = random.choice(choices)

        print("User choice: ", user_choice)
        print("Computer choice: ", computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print("User score: ", user_score)
        print("Computer score: ", computer_score)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

game()
