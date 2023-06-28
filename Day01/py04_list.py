# 리스트 []
import datetime

value = datetime.datetime.now()
lists = [1, 2, 3, 4, [5, 6, 7], True, 'Hello', value]

print(lists)
print(lists[-2])
print(lists[-1])

print(lists[4][1])
print(lists[-2][-1])

print(lists[:4])

# 리스트 연산
a = [1, 2, 3]
b = [4, 6, 8]
print(a + b) # => [1, 2, 3, 4, 6, 8] 문자열 합치기
print(a * 2) # => [1, 2, 3, 1, 2, 3] 문자열 반복

a[2] = False
print(a)

# del : 문자열 지우기
del b[2]
print(b)

# --------------------------------------------------------

# 리스트 함수 (문자열 함수만큼 중요)
# (1) append : 리스트에 요소 추가하기
c = [3, 6, 9]
c.append(12)
print(c)

# (2) sort : 정렬
d = [6, 4, 9, 3, 2, 1]

# 오름차순
d.sort()
print(d)
# 내림차순
d.sort(reverse=True)
print(d)

# (3) reverse : 리스트 뒤집기
e = [3, 4, 6, 2, 5]
e.reverse()
print(e)

# (4) index : 인덱스 반환
# index(리스트 값)
f = [3, 4, 6, 2, 5]
print(f.index(4))

# (5) insert : 리스트에 요소 삽입
# insert(인덱스 번호, 값)
# 2번 인덱스에 5.5 추가
f.insert(2, 5.5)
print(f)

# (6) remove : 리스트 요소 제거
# remove(리스트 값)
# 중복되는 값이 있으면 첫번째 요소만 제거
f.remove(3)
print(f)