# 금융가 룰렛 - 누가 계산해야 할까요?
# list와 random 모듈을 사용해서 문제 해결하기

# 1. random.radint는 정수형 사용해야 됨
# 2. list에 저장된 사람의 위치를 사용

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# random_num = random.randint(0,4)
# if random_num == 0:
#     print(friends[0])
# elif random_num == 1:
#     print(friends[1])
# elif random_num == 2:
#     print(friends[2])
# elif random_num == 3:
#     print(friends[3])
# else:
#     print(friends[4])

# 위의 방법과 똑같은 방법이지만 더 간단하게
random_num = random.randint(0,4)
print(friends[random_num])

# random.choice 라는 함수 사용 --> 리스트의 무작위로 대상 선정
# random_name = random.choice(friends)
# print(random_name)    
