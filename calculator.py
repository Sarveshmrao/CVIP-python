# Calculator
"""
Problem Statement:
The objective of this project is to design and develop a calculator application in Python that
allows users to perform basic arithmetic operations such as addition, subtraction,
multiplication, and division. The application should provide a user-friendly interface and
accurate calculations.
"""

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  try:
    return num1 / num2
  except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    return None
print("Welcome to the calculator!")
# above functions are for different operations

# from here the main loop starts
while True:
  num1 = float(input("Enter first number: "))
  operation = input("Choose an operation (+, -, *, /): ")
  num2 = float(input("Enter second number: "))

  if operation == "+":
    result = add(num1, num2)
  elif operation == "-":
    result = subtract(num1, num2)
  elif operation == "*":
    result = multiply(num1, num2)
  elif operation == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operation. Please try again.")
    continue

  print(f"{num1} {operation} {num2} = {result}")

  choice = input("Do you want to perform another calculation? (y/n): ").lower()
  if choice not in ("y", "n"):
    print("Invalid input. Please enter y or n.")
    continue
  elif choice == "n":
    break

print("Thank you for using the calculator!")
