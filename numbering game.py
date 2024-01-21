import random

text = "Welcome to the number guessing game"
line_width = 60
print(text.center(line_width))

a = "I am thinking of a number between 1 and 10"
a_width = 60
print(a.center(a_width))

b = "You have three chances to guess the number"
b_width = 60
print(b.center(b_width))

number = random.randint(1, 10)
chances = 0

while chances < 3:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You won.")
        break
    elif guess < number:
        print("Your guess was too low.")
    else:
        print("Your guess was too high.")

    chances += 1

if chances >= 3:
    print("Sorry, you lose. The correct number was ",number)
