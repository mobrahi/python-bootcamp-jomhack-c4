# basic exception handling 
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(f"Result: {result}")
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Error! Division by zero is not allowed.")

# using finally block
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found! Please check the file path.")
else:
    # If no exception occurs, this block will execute
    content = file.read()
    print("File read successfully.")
finally:
    # This block will always execute
    if 'file' in locals() and not file.closed:
        file.close()        
print("Cleaned up completed.")

# raising exceptions
# age = input("Enter your age: ")

# def validate_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     if age > 150:
#         raise ValueError("Age cannot be greater than 150.")
#     return True

# try:
#     # Convert input to integer before validation
#     age = int(age)
#     validate_age(age)
#     print("Age is valid.")
# except ValueError as e:
#     print(f"Validation Error: {e}")
