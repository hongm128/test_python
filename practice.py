# Q. 댓글 이벤트 진행, 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰 발행,
# 추첨 프로그램 작성하기

# 조건1. 댓글은 20명이 작성, 아이디는 1~20으로 가정
# 조건2. 댓글은 랜덤 추천, 중복 불가
# 조건3. random 모듈의 shuffle과 sample 사용

# Ex An. 
# -당첨자 발표-
# 치킨: 1
# 커피: [2,3,4]
# -축하합니다.-

# 활용 Ex.
# from random import *
# list = [1,2,3,4,5]
# print (list) #[1, 2, 3, 4, 5]
# shuffle (list) 
# print (list) #랜덤으로 섞임
# print(sample (list, 1)) #list에서 랜덤으로 1개만 뽑겠음 

from random import *
event = range(1,21) #1~20까지 숫자 생성
event=list(event)
shuffle (event)

winners = sample(event, 4) #4명 중 1명은 치킨, 3명은 커피
print ("-당첨자 발표-")
print ("치킨: {0}".format(winners[0]))
print ("커피: {0}".format(winners[1:]))
print (" -축하합니다.-")
#-당첨자 발표-
# 치킨: 20
# 커피: [10, 7, 2]
#  -축하합니다.-