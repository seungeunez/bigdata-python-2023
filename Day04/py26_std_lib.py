#표준 라이브러리
# import datetime as dt
from datetime import date, datetime #위의 라이브러리보다 더 잘쓰임

first_date = date(2022, 12, 25)
print(first_date)

cur_date = date.today() # 년월일까지만 나옴 # date type임
print(cur_date)

print(cur_date - first_date) #만난날 구하기

cur_dt = datetime.now() # 더 많이 쓰임 (정확한 날짜 시간을 뽑아서 날짜 따로 시간 따로 뽑아내는 방식을 사용해서 더 많이 쓰이는거임)
print(cur_dt) # 년월일 시분초 다 나옴
print(cur_dt.strftime('%Y-%m-%d')) # date.tody()와 동일하지만 문자열임

print(cur_dt.weekday()) # 0부터 월요일
print(cur_dt.isoweekday()) # 1부터 월요일



import time

for x in range(10):
    print(x)
    time.sleep(0.1) # (1.0)1초마다 데이터 보내기, (0.1) 0.1 초마다 # second C#, java, C++ time.sleep(ms)
    
import math
print(math.pi)

import os
# print(os.environ)
# print(os.environ['PATH'])

print(os.getcwd())
print(os.system('python --version')) #콘솔 명령어 실행


## json 모듈(라이브러리)
import json

data = ''
with open('./Day04/data.json', mode='r', encoding='utf-8') as f:
    data = json.load(f) # load -> str, loads -> byteArray

print(data)


## urllib 라이브러리
from urllib.request import urlopen

res = urlopen('https://www.naver.com') 
print(res.status) # 200 => OK
print(res.read().decode('utf-8')) # index.html 가져옴 --> 웹 크롤링 기초


