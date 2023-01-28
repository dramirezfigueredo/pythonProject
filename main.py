# simple rock, paper, scissors tutorial

import random


exit = False
user_points = 0
computer_points = 0


while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("This is the final score")
        print("User score: " + str(user_points) + "    /    Computer score: "+ str(computer_points))
        print("Goodbye!")
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("You chose rock")
            print("Computer chose rock")
            print("It's a tie!")

        elif computer_input == "paper":
            print("You chose rock")
            print("Computer chose paper")
            print("You lose!")
            computer_points += 1

        elif computer_input == "scissors":
            print("You chose rock")
            print("Computer chose scissors")
            print("You win!")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("You chose paper")
            print("Computer chose rock")
            print("You win!")
            user_points += 1

        elif computer_input == "paper":
            print("You chose paper")
            print("Computer chose paper")
            print("It's a tie!")

        elif computer_input == "scissors":
            print("You chose paper")
            print("Computer chose scissors")
            print("You lose!")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("You chose scissors")
            print("Computer chose rock")
            print("You lose!")
            computer_points += 1

        elif computer_input == "paper":
            print("You chose scissors")
            print("Computer chose paper")
            print("You win!")
            user_points += 1

        elif computer_input == "scissors":
            print("You chose scissors")
            print("Computer chose scissors")
            print("It's a tie!")

    elif user_input != "scissors" or  user_input != "rock" or  user_input != "paper" or  user_input != "exit":
        print("invalid input")







