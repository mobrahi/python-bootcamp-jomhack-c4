fruits = {"apple", "banana", "cherry"}
number_set = {1, 2, 3, 4, 5}

# print(fruits)        # {'apple', 'banana', 'cherry'}
# print(number_set)    # {1, 2, 3, 4, 5}

#fruits.add("orange") # adding an element
# #fruits.reverse() 
# fruits.remove("banana")
# fruits.discard("orange")

#print(fruits) # this will raise an AttributeError since sets do not have a reverse method

# sets are unordered collections of unique elements
# sets are mutable, but elements must be immutable
# sets do not allow duplicate values
# sets support mathematical operations like union, intersection, difference etc.
# sets are defined using curly braces {} or the set() function

# set operations

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.union(set2))          # {1, 2, 3, 4, 5, 6}
# print(set1.intersection(set2))   # {3, 4}
# print(set1.difference(set2))     # {1, 2}
# print(set2.difference(set1))     # {5, 6}

grades = [
    ("Alice", "Math", 85), 
    ("Bob", "Science", 90),
    ("Alice", "Science", 78),
    ("Charlie", "Math", 90), 
    ("Bob", "Math", 88),
    ("Alice", "English", 95)
  ] 

# unique_students = set(student for student, subject, grade in grades) # set comprehension to extract unique student names
# unique_subjects = set(subject for student, subject, grade in grades) # set comprehension to extract unique subjects

# print("Unique Students:", unique_students)  # {'Alice', 'Bob', 'Charlie'}
# print("Unique Subjects:", unique_subjects)  # {'Math', 'Science', 'English  '}

# set comprehension syntax
# new_set = {expression for item in iterable if condition}  

student = set() # empty set to store unique student names
for grade in grades:
    student.add(grade[0]) # adding student names to the set
print("Unique Students:", student)  # {'Alice', 'Bob', 'Charlie'}   

subject = set()
for grade in grades:
    subject.add(grade[1]) # adding subjects to the set
print("Unique Subjects:", subject)  # {'Math', 'Science', 'English  '}  

alice_grades = []
for grade in grades:
    if grade[0] == "Alice":
        alice_grades.append((grade[1], grade[2])) # collecting Alice's grades
print("Alice's Grades:", alice_grades)  # [('Math', 85), ('Science', 78), ('English', 95)        ]

# 🧠 Ask: How would you extract unique grades from the grades list  ?
# unique_grades = set(grade for student, subject, grade in grades)
# print("Unique Grades:", unique_grades)  # {85, 90, 78, 88, 95}      
