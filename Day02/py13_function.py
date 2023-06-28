# 함수
'''
return 값 없으면 private int getMethods(int x, Object y) {
    return result;
}
return 값 없으면 private void ~  
'''

# 함수선언 def 함수명(파라미터) [ -> any] :
def add(x, y) -> any:
    return x + y

def minus(x, y):
    return x - y

print(add(3, 5.4))
print(minus(5, 4))
print(add('Hello', 'World')) # 입력파라미터에 제약이 없음


# 리턴값이 없는 함수
def plus(x, y):
    print(x+y)
    
plus(2, 4)




'''
satic void main(string[] args)
'''
# 다중 파라미터
def add_many(*args): # C/C++ pointer처럼 보이지만 아님
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1, 2, 3))
print(add_many(3, 6, 9, 12, 15, 18, 21))
print(add_many(1, 2, 3, 4 , 5, 6, 7, 8, 9, 10))
print(add_many(4, 3.141592, 50, 123.6))

# print(add_many('Life', 'is', 'short', 'You', 'need', 'Python')) #result = '' 일때만 가능함

# 키워드 매개변수 = 결과가 딕셔너리로 나옴
def print_kwargs(**kwargs):
    return kwargs
    # print(kwargs)

#return kwargs 일 때
result = print_kwargs(a = 1)
print(result['a'])
res = print_kwargs(name = 'Hugo', age = 45)    
print(res.get('name'))
print(res)

#print(kwargs) 일 때
# print_kwargs(a = 1)
# print_kwargs(name = 'Hugo', age = 45)


def mult(x, y):
    return x * y

def div(x, y):
    return x / y

a = 10
b = 7

print(add(a, b))
print(minus(a, b))
print(mult(a, b))
print(div(a, b))

# add, minus, mult, div 함수 네개가 할 일을 하나의 함수로 처리
def all_calc(x, y):
    return (x + y, x - y, x * y, x / y)

print(all_calc(601, 45))
# 함수는 무조건 하나의 값만 리턴했었음
# 리턴값을 튜플로 처리하면 리턴을 한꺼번에 여러개 할 수 있음
(res_add, res_minus, res_mult, res_div) = all_calc(601, 45)




# 함수 기본값
def introduce_myself(name, age, man = True) -> None: # 리턴값이 없어서 None임
    print(f'나의 이름은 {name}입니다')
    print(f'나이는 {age}세 입니다')
    if man:
        print(f'나는 남자입니다')
    else:
        print(f'나는 여자입니다')
    

introduce_myself('이름', 26, False)
introduce_myself(man=False, name='이름', age=25) # 파라미터명을 지정하면 순서는 상관없다


# 같은 이름의 변수를 사용하는 것을 지양할 것

val = 1 # 전역변수

def valtest(val): # 지역변수
    val += 1
    return val

def valtest2():
    global val # 전역변수 val을 내가 함수내에서 잠시 가져다 쓸게!!
    val += 10


res = valtest(val)
print(val)
print(res)

valtest2()
print(val) # 1 -> 11




# lambda 함수

# javascript jQuery 
# $(document).ready = function() { //익명함수
# }

# $(document).ready = () => { //lambda함수
# }
# var adds = () => { return a + b; }


adds = lambda a, b: a + b

# 위의 식과 동일함
# def adds(a, b):
#     return a + b

print(adds(6 ,7))




# 내장함수
print(abs(-3)) # 절대값 abs[olute]
print(all([1, 3, 5, 7, 9]))

for i in [1,3,5,7,0]:
    print(i)
    

