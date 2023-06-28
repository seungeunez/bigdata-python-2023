# 점프 투 파이썬 - 112 페이지

# 1번 - 평균 구하기
hong = {'국어' : 80, '영어' : 75, '수학' : 55}
print(hong.values())

sum = 0
for item in hong.values():
    sum += item

print(f'홍길동의 평균점수는 {sum / 3} 입니다')

# 2번 - 홀수 짝수 판별
a = 13

result = a % 2 

if result == 1:
    print ("홀수")
else:
    print("짝수")
    
# 2번 강사님st
number = 13
result1 = 13 % 2 == 0
print(f'{number}은 짝수? {result1}')
    
    
# 3번 - 문자열 나누기
pin = "881120-1068234"
yyyymmdd = pin.split('-')[0]
num = pin.split('-')[1]

print(yyyymmdd) #연월일
print(num) # 숫자


# 6번 - 정렬
a = [1, 3, 5, 4, 2]

a.sort()
print(a)

a.sort(reverse=True) 
print(a)


# 11번 - 중복 제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a) # a 리스트를 집합 자료형으로 변환
b = list(aSet) # 집합 자료형을 리스트 자료형으로 다시 변환

print(b)