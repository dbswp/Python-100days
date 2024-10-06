# 기본적인 for문
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# for friend in friends:
#     print(friend) 

# for문을 사용해서 리스트의 max()기능 만들어보기
# scores = [1,15,789,324,584,9,58,46,54,23,48,3,48,742,48,38,5,4,67,4,321]

# max_score = 0
# for score in scores:
#     if score > max_score:
#         max_score = score

# print(max_score)

# range Function with For loop

# 3,5의 약수와 15의 약수 찾기

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)