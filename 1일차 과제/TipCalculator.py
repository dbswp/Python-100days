# 변수의 데이터 타입과 연산 관련 과제

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How much people to split the bill? "))

price = (total_bill * (tip / 100) + total_bill) / people
final_price = round(price, 2)

print(f"Each person should pay: ${final_price}")