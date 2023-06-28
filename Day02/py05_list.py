# 리스트 계속

a = [1, 2, 3]
print(a)

# 자료구조 stack에 있는 pop 기능 구현 
print(a.pop()) # 리스트 맨 마지막 요소를 꺼내라 
print(a)

a.append(10)
print(a)

print(a.count(2)) # 리스트 안에 있는 값이 몇 개 있는지 확인 (값이 없으면 0으로 나옴)

# 리스트 확장 a = 1, 2, 10
a.extend([5, 3, 2])
print(a)

print(a.count(2))