print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L: ")
pepperoni = input("do you want pepperoni on your pizza? Y, N: ")
ex_cheese = input("extra cheese? Y, N: ")

pay = 0

# if size == "S":
#     pay += 15
#     if pepperoni == "Y":
#         pay += 2
# elif size == "M":
#     pay += 20
#     if pepperoni == "Y":
#         pay += 3
# elif size == "L":
#     pay += 25
#     if pepperoni == "Y":
#         pay += 3
# else:
#     print("Nah")
    
# if ex_cheese == "Y":
#     pay += 1

if size == "S":
    pay += 15
elif size == "M":
    pay += 20
elif size == "L":
    pay += 25
else:
    print("nah")
    
if pepperoni == "Y":
    if size == "S":
        pay += 2
    else:
        pay += 3

if ex_cheese == "Y":
    pay += 1


print(f"Your final bill: ${pay}")
    