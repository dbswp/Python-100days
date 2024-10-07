import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many latters would you like in your password? \n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level
new_password = ""
for i in range(nr_letters):
    rL = random.choice(letters)
    new_password += rL
for j in range(nr_numbers):
    rN = random.choice(numbers)
    new_password += rN
for k in range(nr_symbols):
    rS = random.choice(symbols)
    new_password += rS
    
print(new_password)

random_password = []
for i in new_password:
    random_password.append(i)

# randeom.suffle 함수를 사용해서 간단하게 해결
random.shuffle(random_password)
print(random_password)

my_password = ""
for i in random_password:
     my_password += i
print(my_password)