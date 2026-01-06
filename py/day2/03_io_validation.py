# name = input("Enter your name: ")
# height = float(input("Enter your height in meters: "))

# while True:
#     try:
#         age = int(input("Enter your age in years: "))
#         if age > 0:
#             break
#         else:
#             print("Please enter a valid age between 1 and 119.")
#     except ValueError:
#         print("Invalid input. Please enter a numeric value for age.")

# print(f"Hello, {name}! You are {age} years old and {height} meters tall.")

# calculator = input("Enter a mathematical operation (+, -, *, /): ")
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))    

# Simple Calculator

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Simple calculator 

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero!")
        exit()
else:
    print("Invalid operation!")
    exit()

print("Result:", result)

# Simple Quiz Program

score = 0

# Question 1
print("1. What is the capital of France?")
answer1 = input("Your answer: ")

if answer1.lower() == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Paris.\n")

# Question 2
print("2. What is 5 + 7?")
answer2 = input("Your answer: ")

if answer2 == "12":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 12.\n")

# Question 3
print("3. Which language is this quiz written in?")
answer3 = input("Your answer: ")

if answer3.lower() == "python":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Python.\n")

# Display final score
print("Quiz finished!")
print("Your final score:", score, "/ 3")

score = 0

# # Question 1
answer1 = input("What is the capital of France? ").lower()
if answer1 == "paris":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Wrong! The answer is Paris.")

# # Question 2
answer2 = input("What is 5 + 3? ")
if answer2 == "8":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Wrong! The answer is 8.")

# # Question 3
answer3 = input("What color do you get when you mix red and blue? ").lower()
if answer3 == "purple":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is purple.")

# Final score
print(f"\nYour final score: {score}/3")
if score == 3:
    print("Perfect score!")
elif score >= 2:
    print("Good job!")
else:
    print("Better luck next time!")

