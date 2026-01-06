# age = 18

# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

# score = 85

# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'F'     

# print(f"Your grade is: {grade}")

# user_age = 25
# has_license = True

# if user_age >= 18 and has_license:
#     print("You are eligible to drive.")
# else:
#     print("You are not eligible to drive.")

# day = "Saturday"
# if day == "Saturday" or day == "Sunday":
#     print("It's the weekend!")
# else:
#     print("It's a weekday.")

# BMI Calculator

# weight = float(input("Enter your weight (kg): "))
# height = float(input("Enter your height (m): "))


# Get user input
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Categorize BMI
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

# Output the result
print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")