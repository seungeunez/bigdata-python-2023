# 내장함수
print(abs(-4)) # 절대값
print(chr(65)) # 숫자를 캐릭터로 변경 65 A, 97 a - ascii 코드 번호
print(chr(44086)) # utf-8 코드
print(chr(13)) # enter
print(min(1, 4)) # 최소값
print(max(1, 4)) # 최소값
print(eval('1 + 4')) # eval[uate] 실행
print(hex(234)) # 16진수

a=0
b=1
print(id(a)) # a변수의 메모리 주소
print(id(b)) # b변수의 메모리 주소

print(int('3')) #digit number 문자열을 정수로 변환

print(pow(2, 10)) #제곱승 함수 # 2^10
print(2 ** 10) #제곱승  # 2^10


#map
def three_times(numberlist):
    result = []
    for n in numberlist:
        result.append(n * 3)
    return result

l1 = [3, 6, 9, 12]
print(three_times(l1)) #함수가 파라미터로 리스트 받아서 for문으로 전부 처리

def threetimes(x):
    return x * 3

print(list(map(threetimes, l1))) 
# 함수를 첫 번째 파라미터로, 두 번째를 적용시킬 리스트로
# 리스트 요소 하나씩을 함수를 통해서 처리를 해주는 방법



# map결과가 map object 이기 때문에 list, tuple, set으로 형변환 필요
print(list(map(str, l1)))
print(tuple(map(float, l1)))
print(set(map(float, l1)))


# range list 두개를 잘 활용하면 순차적 리스트를 쉽게 만들 수 있음
print(list(range(10)))
print(list(range(3, 100, 3))) # 3의 배수 99까지
print(sum(list(range(3, 100, 3)))) # 3의 배수 99까지 합계

'''
result = 0
i = 1
    
while i <= 1000:
    if i % 3 == 0:
        result += i
        #print(i, end=', ')
    i += 1
    
print(result)
'''
#이것도 3의 배수 99까지의 합계임


#반올림
print(round(4.6))
print(round(3.141422, 4)) #소수점 4번째 자리에서 반올림하겠다는 뜻


# 정렬
l1.sort()
sorted(l1)


# 변수/값의 타입을 리턴
print(type(21))
print(type('21'))
print(type(True))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type(None))