import random

for item in range(20):
    number = random.randint(1, 100)
    print(number, end="\t")

text = "hello world"
sides = "$" * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = "*" * len(formatted_text)

print(top_bottom)
print(formatted_text)
print(top_bottom)
