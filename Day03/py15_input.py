# 입출력
import datetime # 날짜를 확인하기 위한 라이브러리 (날짜 모듈) 가져옴

# birth_year = input('출생년도를 입력하세요 > ') # 키보드 입력 (키보드 입력되는건 무조건 문자열임)

birth_year = 1998 # int(input('출생년도를 입력하세요 > ')) # 키보드 입력 ( age = curr_year - birth_year 을 위해서 형변환 해줘야함)

print(f'당신의 출생년도는 {birth_year}년입니다.') # 콘솔 출력

curr_year = datetime.datetime.now().year # {}는 모듈을 뜻함 # now()까지만 하면 yyyy-MM-dd hh:mm:ss.ms까지 나옴

print(f'올해는 {curr_year}년도입니다') # 현재년도 출력

age = curr_year - birth_year
print(f'당신의 나이는 {age}세 입니다.')



a = 123
a = [3, 6, 9]
print(a)


print('Life' 'is' 'short')
print('Life' + 'is' + 'short') # 위와 동일함 (공백이 없음)
print('Life', 'is', 'short') # 이렇게 쓰자 (공백 있음)

print((range(10))) # range(0, 10)
print(len(range(10))) # 10

for i in range(10):
    if i == (len(range(10)) - 1):
        print(i, end='\n') # 엔터를 없앨 때 end씀
    else:
        print(i, end=', ')
        
print('Life', 'is', 'short', sep='&') # 단어 사이 구분자로 쓸 때 sep 씀 (sep 별로 안쓰임)



pi = 3.14159265359

print(f'PI - {pi:.4f}') # format string # .4f는 소수점 4번째 자리까지 출력 됨
print(f'PI - {pi:10.2f}') 
