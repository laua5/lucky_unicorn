""" Component 2 (how much) v3
More efficient method - includes valid range as the basis of the while loop
which eliminates the need to use the 'valid' variable """

error = "That was not a valid input\n"
user_balance = 0

# Keep asking until a valid amount (1-10) is entered
while not 1 <= user_balance <= 10:
    try:
        # ask for amount
        user_balance = int(input("Please enter a whole number between 1 and 10"
                                 "\nHow much would you like to play with? $"))

        print()

    except ValueError:
        print(error)

print(f"You are play with ${user_balance}")
