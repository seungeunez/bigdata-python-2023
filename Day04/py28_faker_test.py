from faker import Faker
import pandas as pd
import os

#가짜 데이터를 만들어줌
dummy = Faker('ko-KR')
# print(dummy.name())
# print(dummy.address())
# print(dummy.company())

dummy_data = [[dummy.name(), dummy.postcode(), dummy.address(), 
                dummy.phone_number(), dummy.email()] for i in range(1000)]

df = pd.DataFrame(data=dummy_data, columns=['이름','우편번호','주소','전화번호','이메일'])

# print(dummy_data)

df.to_csv('./Day04/dummy_members2.csv', index=True, encoding='utf-8') # index=True면 앞에 번호가 붙음 (보통 0부터 시작함) #.csv 파일 생성
print('CSV 생성완료')

# data = pd.read_csv('./Day04/dummy_member2.csv', encoding='utf-8')
# print(data)
