#변수에 대하여

a = 1
b = 'python'
c = [1, 2, 3]

print(id(a))
print(id(b))
print(id(c))


# 문자열은 할당, copy 동일 / 리스트는 할당, copy가 다름

a = c
print(id(a))
print(id(c))
print(a is c)


from copy import copy

a = copy(c)
print(id(a))
print(id(c))
print(a is c)

(a, b) = ('python', 5)

print(a, b)

[c, d] = ['python', 7]

print(d)