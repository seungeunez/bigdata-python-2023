# 튜플
# 리스트와 유사하지만 추가, 수정, 삭제가 불가능 함 그걸 immutable이라고 부름 (가능하면 mutable이라고 함)

l1 = [1, 2, 3]
t1 = (1, 2, 3)

l1.append(4) # 리스트 함수는 11개 있음 (이유: 수정이 가능하니깐)
# 튜블은 추가, 수정, 삭제가 불가능하니깐 함수가 리스트에 비해 적음 # 튜플 함수중에 __ 로 시작하는건 신경안써도 됨 (튜플 함수 2개라고 생각하면 됨)

del l1[0]
print(l1)

# del t1[0] # 예외 발생
print(t1[2])
print(t1[:2]) # 마지막 값의 인덱스 -1 까지

t2 = (5, 6, 7)
t3 = t1 + t2 # 새로운 튜플을 최초에 만드는 연산은 가능함
print(t3)

# t3[4] = 55 # 이미 만들어진 튜플에 추가는 불가능함

def calc(x, y):
    #사칙연산 모두 다 처리
    add = x + y
    minus = x - y
    mult = x * y
    div = x / y
    
    return(add, minus, mult, div)

#값을 한꺼번에 여러개 리턴받을 수 있음 (java, c#, python 동일)
res1, res2, res3, res4 = calc(5, 8)

print(res1, res2, res3, res4)