# 문자열

value = "Hello World"
print(value)
print('Hello World')

print('저는 "탁승은"입니다')
print('저는 \'탁승은\'입니다')

# 여러줄 문자열
value = '''
안녕하세요.
반가와요.
잠이 와요.
'''

print(value)

# 문자열 합치기
print('Hello' + ' World!')

# 예외 발생
# print('Hello' + 4)

# 문자열 반복
print('Hello' * 4)

# len() : 문자열 길이 (공백도 길이 하나로!)
print(len('Life is short'))

# -------------------------------------------------------------

# 인덱싱
origin = 'Life is short, You need Python'
print(origin[0])
print(origin[13])
print(origin[0] + origin[16] + origin[19] + origin[20] + origin[0].lower() + origin[15].lower())

# 슬라이싱
# [시작값 : 끝 값 + 1]
print(origin[0:4])
print(origin[:4])
print(origin[8:13])
print(origin[15:])
print(origin[15:-7]) # 음수 => 뒤에서부터 인덱스 -1부터 시작

# -------------------------------------------------------------

# 포맷팅
# %s : 문자
print("I ate %s apples" % ('three'))

# %d : 정수(Integer)
print("I ate %d apples" % (3))

# %f : 실수
print("pi is %f" % 3.14159265359) # => pi is 3.141593
print("pi is %10.2f" % 3.14159265359) # => pi is       3.14 => 문자열 총 길이 10, 소수점 아래 두번째까지

# -------------------------------------------------------------

# 날짜 문자열 포맷팅
import datetime as dt

curr_dt = dt.datetime.now()
print(curr_dt)
print('오늘 날짜는 %s 입니다' % (curr_dt))
print('오늘 날짜는 %s 입니다' % (curr_dt.strftime('%Y년 %m월 %d일')))

# 최신 포맷팅
apple_num = 3
print(f'I ate {apple_num} apples')
print(f'I ate {apple_num:0.4f} apples')

fmt_dt = curr_dt.strftime('%Y년 %m월 %d일')
print(f'오늘 날짜는 {fmt_dt} 입니다')

# -------------------------------------------------------------

# 'Life is short, You need Python'
# 문자열 함수
# (1) count : 문자나 문자열 개수 세기
print(origin.count('o'))
print(origin.count('need'))

# (2) find : 위치 알려 주기 1
# 문자나 문자열 찾기 => 인덱스값을 반환함
# 없는 경우 : -1 
# 대소문자를 구분함
print(origin.find('python')) 
print(origin.find('Python')) 

# (3) index : 위치 알려 주기 2

# (4) join : 문자나 문자열을 join에 있는 문자열과 하나씩 합침
print('/'.join(origin))

# (5) upper : 전부 대문자로 변환
print(origin.upper())

# (6) lower : 전부 소문자로 변환
print(origin.lower())

# (7) capitalize : 문자열의 첫번째 단어의 첫번째 글자만 대문자로 변환
print(origin.capitalize())

# (8) title : 문자열의 단어 중 첫번째 글자만 대문자로 변환
print(origin.title())

# (9) lstrip : 왼쪽 공백 지우기
print('start' + '    Hello    '.lstrip() + 'end')
# (10) rstrip : 오른쪽 공백 지우기
print('start' + '    Hello    '.rstrip() + 'end')
# (11) strip : 양쪽 공백 지우기
print('start' + '    Hello    '.strip() + 'end')

# (12) split : 문자열 나누기
# 문자열이 나누어진 후 배열화됨
result = origin.split(' ')
print(result)

# (13) replace : 문자열 바꾸기
# replace(A, B) => A를 B로 바꿈
a = "Life is too short"
print(a.replace("Life", "Your leg"))
