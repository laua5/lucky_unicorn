"""LU Yes/No
Simplifies the input by converting it into lower case. Also accepts y or n as
abbreviations. Prints result of user choice as well as input for testing
"""


# Ask the user if they have played before
show_instructions = input("Have you played this game before?: ").lower()

# If they say yes, output 'Program Continues'
if show_instructions == "yes" or show_instructions == "y":
    print("program continues")

# If they say no, output "Display Instructions"
elif show_instructions == "no" or show_instructions == "n":
    print("Display instructions")

# Otherwise - Show error
else:
    print("Please answer 'yes' or 'no'")

print(f"You entered '{show_instructions}'")
