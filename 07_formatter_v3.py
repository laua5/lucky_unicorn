""" Component 5 - statement formatter v3
call function 3 times - one for each of the tests
"""


# Function to format into text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()
print(formatter("!", "Congratulations, you got a unicorn"))
print()
print(formatter("*", "Goodbye"))
