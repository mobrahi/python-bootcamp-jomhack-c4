# for loop
# for i in range(5):
#     print("Iteration:", i)

# for i in range(1, 6):
#     print("Number:", i)

# for i in range(2, 10, 2):
#     print("Even number:", i)

# count = 0
# while count < 5:
#     print("Count is:", count)
#     count += 1

# while loop
# count = 0
# while count < 5:
#     print("Current count:", count)
#     count += 1

# loop control statements
# for i in range(10): 
#     if i == 3:
#         continue  # skip the rest of the loop when i is 3
#     if i == 7:
#         break  # exit the loop when i is 7
#     print(i) 

# nested loops
# for i in range(2):
#     for j in range(3):
#         print(f"(i: {i}, j: {j})")

# Multiplication Table Generator

# Get the number from the user
# try:
#     num = int(input("Enter the number for the multiplication table: "))
# except ValueError:
#     print("Please enter a valid integer!")
#     exit()

# # Get the range (how far the table should go)
# try:
#     limit = int(input(f"Up to what number should the table go? (default 12): ") or "12")
# except ValueError:
#     limit = 12

# # Print the multiplication table
# print(f"\nMultiplication Table for {num}:\n")
# print("-" * 30)

# for i in range(1, limit + 1):
#     print(f"{num} × {i:2} = {num * i}")

# print("-" * 30)

# Prime Numbers Finder (up to a given limit)

# def find_primes(limit):
#     if limit < 2:
#         print("No prime numbers below 2.")
#         return []
    
#     # Sieve of Eratosthenes
#     is_prime = [True] * (limit + 1)
#     is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
#     for i in range(2, int(limit ** 0.5) + 1):
#         if is_prime[i]:
#             # Mark multiples of i as non-prime
#             for j in range(i * i, limit + 1, i):
#                 is_prime[j] = False
    
#     # Collect and return prime numbers
#     primes = [i for i in range(2, limit + 1) if is_prime[i]]
#     return primes

# # Set the limit (you can change this value)
# limit = 100

# Find and display primes
# prime_list = find_primes(limit)

# print(f"Prime numbers up to {limit}:")
# print(prime_list)
# print(f"Total: {len(prime_list)} primes")

# Simple Prime Numbers Finder (up to a given limit)

# def find_primes_simple(limit):
#     primes = []
#     for num in range(2, limit + 1):
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     return primes

# # Usage
# try:
#     n = int(input("Enter the upper limit: "))
#     primes = find_primes_simple(n)
#     print("Primes:", primes)
#     print("Count:", len(primes))
# except ValueError:
#     print("Invalid input!")

limit = 20

for num in range(3, limit + 1):
    is_prime = True
    for i in range(2, num ):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')