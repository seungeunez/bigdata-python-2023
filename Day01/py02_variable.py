# 변수
import sys

number = 10000000000000000

# sys.maxsize : 파이썬 시스템에서 제공하는 최고 숫자
value = sys.maxsize 

print(number)
print(value)
print(value + 1)

# ------------------------------------------------------

# 8진수 0o
value2 = 0o12

print(value2)

# ------------------------------------------------------

# 16진수 0x
value2 = 0xFF

print(value2)

# ------------------------------------------------------

value2 = 'Hello, Python'

print(value2)

# ------------------------------------------------------

value2 = False

print(value2)
print(value2 == False)
print(value2 == True)

# ------------------------------------------------------

# 나누기
print(20 / 3)   # 소수점 O
print(21 // 3)  # 소수점 X

# 거듭제곱
print(2 ** 10)

# 나머지
print (10 % 3)