student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Science", "English"] 
    }

# print(student["name"]) # Output: Alice # Accessing value by key  
# print(student.get("age")) # Output: 20 # Using get() method
# student["age"] = 21 # Modifying existing key-value pair
# student["email"] = "alice@example.com" # Adding new key-value pair
# print(student)

# # dictionary methods
# keys = student.keys() # Get all keys
# values = student.values() # Get all values
# items = student.items() # Get all key-value pairs

# print(keys)
# print(values)
# print(items)

# iterating through a dictionary

# for key in student: # iterating through keys
#     print(f"{key}: {student[key]}")

# for key, value in student.items(): # iterating through key-value pairs
#     print(f"{key}: {value}")

# nested dictionaries

# company = {
#     "employee": {
#         "John": {"age": 30, "departments": "IT"},
#         "Jane": {"age": 25, "departments": "HR"}
#     },
#     "department": ["IT", "HR", "Finance"]
# }
# print(company["employee"].items())
# print(company["employee"]["Jane"]["departments"]) # Accessing nested dictionary
# print(company["department"]) # Accessing list within dictionary
# print(company["employee"]["John"]["age"]) # Accessing nested value

# for key, value in company["employee"].items(): # Iterating through nested dictionary
#     print(f"{key}: {value}")

# exercise

# student_records = {
#     "001": {"name": "John", 
#             "age": 19, 
#             "major": "Computer Science", 
#             "grade": [85, 92, 78]},
#     "002": {"name": "Sarah", 
#             "age": 20, 
#             "major": "Biology",
#             "grade": [90, 88, 95]}
# }

# print(student_records)

# # Add a new student record  

# student_records["003"] = {
#     "name": "Mike", 
#     "age": 18, 
#     "major": "Mathematics", 
#     "grade": [82, 79, 91]}

# print(student_records)

# # loop and print student details in the specified format:

# for student_id, student_info in student_records.items(): 
#     print(f"Student ID: {student_id}") 
#     print(f" Name: {student_info["name"]}") 
#     print(f" Major: {student_info["major"]}") 
#     print()

# Nested loops example: printing coordinates in a grid

for row in range(1, 4):        # Outer loop → rows
    for col in range(1, 4):    # Inner loop → columns
        print(f"({row},{col})", end=" ")
    print()  # Move to next row

