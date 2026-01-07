coordinates = (10, 20)
person = ("Alice", 30, "Engineer")
single_element_tuple = (42,) # Note the comma

# tuple operations
print(coordinates[0])  # Output: 10 # Accessing first element
print(len(person))     # Output: 3 # Length of the tuple
print(person[2])    # Output: Engineer # Accessing third element
print(single_element_tuple)  # Output: (42,)
print(coordinates.append(30))  # This will raise an AttributeError since tuples are immutable