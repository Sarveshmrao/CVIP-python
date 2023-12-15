# Random Password Generator
"""
Problem Statement:
The objective of this project is to design and develop a random password generator
application that allows users to generate strong and secure passwords with various criteria.
The application should provide options for password length, character types, and special
requirements.
"""

import random
import string

def generate_password(length, lowercase=True, uppercase=True, numbers=True, symbols=True):
  # define the characters to use in the password
  characters = ""
  if lowercase:
    characters += string.ascii_lowercase
  if uppercase:
    characters += string.ascii_uppercase
  if numbers:
    characters += string.digits
  if symbols:
    characters += string.punctuation
    # generate the password
  password = "".join(random.choice(characters) for _ in range(length))
  return password

# get input from user
desired_length = int(input("Enter desired password length (minimum 8): "))
lowercase = input("Include lowercase letters (y/n)? ").lower() == "y"
uppercase = input("Include uppercase letters (y/n)? ").lower() == "y"
numbers = input("Include numbers (y/n)? ").lower() == "y"
symbols = input("Include special symbols (y/n)? ").lower() == "y"

# generate the password and print it
password = generate_password(desired_length, lowercase, uppercase, numbers, symbols)
print(f"Your randomly generated password: {password}")
print("Thank you for using the password generator!")
