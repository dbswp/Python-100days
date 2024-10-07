# Hang Man 만들기

# 1. 무작위 단어 고르기
import random
word_list = ["aardvark", "baboon", "apple"]
word_L = []

word = random.choice(word_list)
for i in range(len(word)):
    print("_", end='')
    word_L.append("_")
    
# 소문자만 사용하기 위해 lower() 함수 사용
# guess_letter = input("\nGuess a letter: ").lower()

# 맞는지 안맞는지 확인하는 방법
# for i in word:
#     if i != guess_letter:
#         print("Wrong")
#     else:
#         print("Right")

# 내가 한 방법 - 리스트 사용해서 해당 인덱스 값의 값 변경
# for i in range(len(word)):
#     if word[i] == guess_letter:
#         word_L[i] = guess_letter
#     else:
#         print("wrong")
game_over = False
life = 3
while not game_over:
    guess_letter = input("\nGuess a letter: ").lower()
    
    if guess_letter in word_L:
        print("이미 입력한 단어입니다.")
        
    for i in range(len(word)):
        if word[i] == guess_letter:
            word_L[i] = guess_letter

    if guess_letter not in word_L:
        life -= 1
        if life < 0:
            game_over = True
            print("Hang Man die")
    
    if "_" not in word_L:
        game_over = True
        print("you win")
            
    c_word = ''
    for i in word_L:
        c_word += i
    print(word_L)
    print(c_word)

    
# 강의가 한 방법 - 문자열로 풀이
# display = ""
# for i in word:
#     if i == guess_letter:
#         display += i
#     else:
#         display += "_"

# print(word_L)
# print(c_word)