# # Nested Loops and Control Flow Example

# for x in range(3): # Outer loop (Rows)
#     for y in range(2): # Inner loop (Columns)
#         print(f"x is {x}, y is {y}")

# # Demonstrating 'continue' and 'break' statements

# numbers = [10, -5, 30, 40, -2, 50]
# target = 40

# for num in numbers:
#     if num < 0:
#         continue  # Skip the negative numbers
    
#     print(f"Checking {num}...")
    
#     if num == target:
#         print("Found it!")
#         break  # Stop the loop early because we found what we needed

# Multiplication Table using Nested Loops


# for i in range(1,6): # Print the multiplication table from 1 to 5
#     for j in range(1,6): # Inner loop for each multiplier
#         product = i * j # Calculate the product

#         if product % 2 == 0: # Check if the product is even
#             print("X", end="\t") # Print 'E' for even products with a tab space
#         else:
#             print(product, end="\t") # Print the product with a tab space
#     print()  # New line after each row

# Number Guessing Game

# import random

# # The computer picks a random number between 1 and 10
# secret_number = random.randint(1, 10)
# guess =  0 # Initialize the variable so the loop can start

# print("I'm thinking of a number between 1 and 10.")

# # The loop continues as long as the guess is NOT the secret number
# while guess != secret_number:
#     # Ask the user for a guess (and convert it to an integer)
#     guess = int(input("Enter your guess: "))
    
#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed it.")

# Sum of even numbers from 0 to 4 using a while loop
#    
# x = 0
# total = 0
# while x < 5:
#     if x % 2 == 0:
#         total += x
#     x += 1
# print("The sum of even numbers from 0 to 4 is:", total)

# Explanation of Control Flow:

# IF condition is true
#     THEN do this
# ELSE
#     do something else

# Flowchart Representation:

# Start
#   ↓
# Get user input
#   ↓
# Calculate result
#   ↓
# Is result < X?
#  ├─ Yes → Output A
#  └─ No → Is result < Y?
#           ├─ Yes → Output B
#           └─ No → Output C

# Problem-Solving Template:

# 1. INPUT:
#    - What data do I need?

# 2. PROCESS:
#    - What calculations?
#    - What decisions?

# 3. CONDITIONS (If / Else):
#    - If __________ then __________
#    - Else if __________ then __________
#    - Else __________

# 4. OUTPUT:
#    - What should be displayed?

# 5. EDGE CASES:
#    - Smallest value?
#    - Largest value?
#    - Invalid input?

# Example: Traffic Light Decision

# traffic_light = input("Enter light color (red, yellow, green): ").lower()

# if traffic_light == "red":
#     print("Stop")
# elif traffic_light == "yellow":
#     print("Slow down")
# elif traffic_light == "green":
#     print("Go!")
# else:
#     print("Invalid color")

# Example: Discount Calculation

# amount = float(input("Total amount spent?: "))

# if amount >= 500:
#     discount = amount * 0.20
#     print(f"You get a 20% discount of ${discount:.2f}!")
# elif amount >= 300:
#     discount = total_amount * 0.10
#     print(f"You get a 15% discount of ${discount:.2f}!")
# else:
#     print("No discount available.")

# Example: Eligibility Check

# age = int(input("Enter age: "))
# score = int(input("Enter score: "))

# if age < 18:
#     print("Not eligible")
# elif age >= 18 and score >= 60:
#     print("Eligible")
# else:
#     print("Not eligible")
    
# Example: Temperature Classification

# temp = int(input("Enter temperature in Celsius: "))

# if temp < 0:
#     print("Freezing")
# elif temp >= 0 and temp <= 25:
#     print("Cool")
# else:
#     print("Hot")

# Example: Simple Calculator

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# calculation = input("Enter operation (+, -, *, /): ")   

# if calculation == "+":
#     result = num1 + num2
#     print(f"The result is: {result}")
# elif calculation == "-":
#     result = num1 - num2
#     print(f"The result is: {result}")
# elif calculation == "*":
#     result = num1 * num2
#     print(f"The result is: {result}")
# elif calculation == "/":
#     if num2 != 0:
#         result = num1 / num2
#         print(f"The result is: {result}")
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Invalid operation selected.")    
