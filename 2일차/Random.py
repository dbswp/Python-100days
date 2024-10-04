import random

# random.randint(int a, int b) 입력받고 a,b 사이의 무작위 정수 추출
# random_num = random.randint(1,7)
# print(random_num)

# random.random() 0,1 사이의 무작위 부동의 실수
# random_num = random.random()
# print(random_num)

# random.uniform(int a, int b) 입력받고 a,b를 포함한 사이의 무자위 실수 추출
# random_float = random.uniform(1,10)
# print(random_float)

# 동전 앞뒤면 뽑기
random_coin = random.randint(1,2)
if random_coin == 1:
    print("Heads")
else:
    print("Talis")