# # This is a simple demonstration of functions in Python.
# def greet_person(name):
#     print(f"hello, {name}!")

# greet_person("Alice")
# greet_person("Bob")

# Function with return value
# def add_numbers(a, b):
#     return a + b

# result_1 = add_numbers(5, 3)
# result_2 = add_numbers(10, 15)
# print(f"The sum is: {result_1}") 
# print(f"The sum is: {result_2}")

#Function with default parameter
# def greet_with_title(name, title="Mr."): # default title is "Mr."
#     return f"hello, {title} {name}!" # returns a greeting string return

# print(greet_with_title("Smith")) # uses default title "Mr."  
# print(greet_with_title("Johnson", "Dr.")) # uses provided title "Dr."

# *args Function with variable number of arguments
# def sum_all(*args): # accepts variable number of arguments    
#  return sum(args) # returns the sum of all arguments

# print(sum_all(1, 2, 3, 4, 5)) # outputs 15

# # **kwargs Function with keyword arguments
# def print_person_info(**kwargs): # accepts variable keyword arguments    
#  for key, value in kwargs.items(): # iterates through key-value pairs        
#      print(f"{key}: {value}") # prints each key-value pair

# print_person_info(name="Alice", age=30, city="New York")

# combining *args and **kwargs
# def flexible_function(*args, **kwargs): # accepts both variable arguments and keyword arguments
#     print("Positional Arguments:", args) # prints the positional arguments    
#     print("Keyword Arguments:", kwargs) # prints the keyword arguments      

# flexible_function(1, 2, 3, name="Alice", age=25)

# Prime number checker function
# def prime_checker(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# # keep asking until valid integer is entered
# while True:
#     try:
#         number = int(input("Enter a number: "))
#         break  # exit loop once input is valid
#     except ValueError:
#         print("Error: You must enter an integer. Please try again.")

# if prime_checker(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

# temperature conversion function
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


temp_c = float(input("Enter temperature in Celsius: "))
print(f"{temp_c}°C is {celsius_to_fahrenheit(temp_c)}°F")

temp_f = float(input("Enter temperature in Fahrenheit: "))
print(f"{temp_f}°F is {fahrenheit_to_celsius(temp_f):.2f}°C")
