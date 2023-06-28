# 제어문
# 파이썬은 들여쓰기로 제어문, 함수, 클래스의 구역에 들어있는지를 판별 (클래스는 안배움 알아서 공부하시길)

money = True

if(money == True): # 콜론이 나오면 제어문, 함수, 클래스의 시작이다
    print('택시를 탑니다')
elif(money == False): # java와 비교할 것 else if()
    print('걸어갑니다')
else:
    print('나도 몰라')

print('여기서 내립니다') # 탭이 중요!
    
print(3 in [1, 2, 4, 5, 6, 7]) #리스트 안에 3이 있는가?

while(money == True):
    print('와 부럽다')
    break
    
print('\n\n\n')

#java for (int i = 0; i < 10; i++)
for i in range(0, 10):
    print(i)
    

print('\n')


l1 = [1, 3, 5, 7, 9]
for i in l1:
    print(i)

print('\n')

#홀수
print('홀수만 찍기')
for j in range(1 ,10, 2):
    print(j)
    

#구구단
print('구구단')
for x in range(2 ,10): # 2단부터 9단까지
    for y in range(1, 10): # 1부터 9까지
        print(f'{x} x {y} = {x * y:2d}', end=' ')
        
    print('')
    
#연습문제 146페이지

# 2번 - 3의 배수의 합
result = 0
i = 1

# 개수부터 구하기
# while i <= 1000:
#     if i % 3 == 0:
#         result += 1
#     i += 1
# print(result) # 1~1000사이의 3의 배수는 333개
    
while i <= 1000:
    if i % 3 == 0:
        result += i
        #print(i, end=', ')
    i += 1
    
print(result)

# 3번
for i in range (1, 6):
    print('*' * i)