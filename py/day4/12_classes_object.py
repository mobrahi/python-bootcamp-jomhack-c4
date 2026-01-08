# Basic class definition and object instantiation in Python
# class Person:
#     #class attributes
#     species = "Homo sapiens"

#     # constructor method    
#     def __init__(self, name, age):
#         #instance attributes
#         self.name = name
#         self.age = age

#     # instance method
#     def introduce(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."
    
#     # method with parameters
#     def have_birthday(self):
#         self.age += 1
#         return f"Happy birthday {self.name}! You are now {self.age}."
    
# # creating objects (instances of the class)
# person1 = Person("Alice", 30)
# person2 = Person("Bob", 25)

# # accessing attributes
# print(person1.name) # Alice
# print(person1.age) # 30

# # calling method
# print(person1.introduce()) # Hello, my name is Alice and I am 30 years old.
# print(person1.have_birthday()) # Happy birthday Alice! You are now 31.

# # class attributes
# print(Person.species) # Homo sapiens
# print(person1.species) # Homo sapiens

# creating a BankAccount class
# class BankAccount:
#     def __init__(self, account_number, owner, balance=0):
#         self.account_number = account_number
#         self.owner = owner
#         self.balance = balance
#         self.transaction_history = []

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             self.transaction_history.append(("deposit", amount))
#             return f"Deposited ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid deposit amount."

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             self.transaction_history.append(("withdraw", amount))           
#             return f"Withdrew ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid withdrawal amount or insufficient funds."

#     def get_balance(self):
#         return f"Account {self.account_number} has a balance of ${self.balance}"
    
#     def get_transaction_history(self):
#         return self.transaction_history
    
# # Using the BankAccount class
# account1 = BankAccount("123456", "Alice", 500)
# print(account1.deposit(200))  # Deposited $200. New balance: $700
# print(account1.withdraw(100)) # Withdrew $100. New balance: $600
# print(account1.get_balance())  # Account 123456 has a balance of $600
# print(account1.get_transaction_history())  # [('deposit', 200), ('withdraw',
    
# # Creating simple game character class
class GameCharacter:    
    def __init__(self, name, health=100, attack=100, heal=100):
        self.name = name
        self.health = health
        self.attack = attack
        self.heal = heal

    def take_damage(self, damage):  
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return f"{self.name} took {damage} damage and now has {self.health} health."   

    def attack_enemy(self, enemy):
        enemy.take_damage(self.attack)
        print(f"{self.name} attacked {enemy.name} for {self.attack} damage.")

    def heal_self(self):
        self.health += self.heal
        print(f"{self.name} healed for {self.heal} points and now has {self.health} health.")

hero = GameCharacter("Knight", health=120, attack=30, heal=20)
villain = GameCharacter("Orc", health=150, attack=25, heal=10)

hero.attack_enemy(villain)
villain.attack_enemy(hero)
hero.heal_self()
