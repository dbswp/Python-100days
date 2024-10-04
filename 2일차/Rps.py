# 가위바위보 게임
import random

rsp = [0, 1, 2]


choose_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
com = random.choice(rsp)

print(com)

if choose_num >= 3 or choose_num < 0:
    print("Take another num")
elif choose_num == 0 and com == 2:
    print("You Win")
elif choose_num == 2 and com == 0:
    print("You Lose")
elif choose_num > com:
    print("You Win")
elif choose_num == com:
    print("You draw")
elif choose_num < com:
    print("You lose")