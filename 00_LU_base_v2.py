"""LU base component - based on 00_LU_base_v1
Components added after they have been created and tested"""

import random


# Functions go here
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output "Display Instructions"
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - Show error
        else:
            print("Please answer 'yes' or 'no'")


# Function to display instructions
def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game will go here")
    print()


# number checking function
def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount (1-10) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Function to generate random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1  # Keep track of rounds
        number = random.randint(1, 100)

        # Adjust balance
        # If the random number is between 1 and 5
        # User gets a unicorn (add $4 to balance)
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4

        # If the random number is between 6 and 36
        # User gets a donkey (subtract $1 from balance)
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1

        # In all other cases the token must be either a horse or a zebra
        # (In both cases subtract $0.50 from balance)
        else:
            # If number is even, set the token to zebra
            if number % 2 == 0:
                token = "zebra"
                balance -= 0.5

            # Otherwise set the token to horse
            else:
                token = "horse"
                balance -= 0.5

        # output
        print(f"Round {rounds_played} Token: {token}, Balance: {balance:.2f}")
        if balance < 1:
            print("\nSorry but you have run out of money")
            play_again = "x"
        else:
            play_again = input("\n Do you want to play another round?\n<enter>"
                               "to play again or 'X' to exit ").lower()

        print()
    return balance


# Main routine go here.....
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

# Ask how much they want to play with
starting_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f" and leave with ${closing_balance:.2f}")
print("Goodbye")
