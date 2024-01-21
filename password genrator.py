import random
import string
titlee="PASSWORD GENERATOR"
print(titlee.center(50))
titleee="Tell us your choices and we will generate a password for you."
print(titleee.center(10))
geet=input("Your name:")
print("HELLO "+geet+"!")
print("Hope you are doing well!")
print("lets generate a password for you!")
def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars, include_name, include_dob, additional_input):
    # Define character sets based on user criteria
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    lowercase_chars = string.ascii_lowercase if use_lowercase else ''
    numbers_chars = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine character sets
    all_chars = uppercase_chars + lowercase_chars + numbers_chars + special_chars

    # Ensure at least one character set is selected
    if not all_chars:
        print("Error: At least one character set must be selected.")
        return None

    # Validate length
    if length < 8:
        print("Error: Password length must be greater than 8 characters.")
        return None

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    # Include user's name in the password if requested
    if include_name:
        user_name = input("Enter your name: ")
        password = user_name + password

    # Include user's date of birth in the password if requested
    if include_dob:
        dob = input("Enter your date of birth (YYYY-MM-DD): ")
        password = dob + password

    # Include additional user input in the password if requested
    if additional_input:
        additional = input("Enter anything else you want to add to the password: ")
        password = additional + password

    return password

# Get user input for password criteria
while True:
    length = int(input("Enter the length of the password (must be greater than 8): "))
    if length > 8:
        break
    else:
        print("Password length must be greater than 8 characters. Please try again.")

use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
include_name = input("Include your name in the password? (y/n): ").lower() == 'y'
include_dob = input("Include your date of birth in the password? (y/n): ").lower() == 'y'
additional_input = input("Include anything else in the password? (y/n): ").lower() == 'y'

# Generate password based on user input
password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars, include_name, include_dob, additional_input)
if password:
    print("Generated Password:", password)
rv="I HOPE YOU LIKE THE PASSWORD"
print(rv.center(50))
print("Thanks for using the password generator!")

