# CSV 파일 읽기
import csv 

# \ufeff가 숨어 있음 이런 경우 encoding='utf-8-sig'로 변경하면 됨

# csvfile = '부산광역시_시내버스_이용건수.csv'
csvfile = '충청북도_푸드뱅크현황.csv'
dirname = './Day03/'

fr = open(f'{dirname}{csvfile}', mode='rt', encoding='utf-8-sig') # cmd 속성의 현재 코드 페이지를 보고 encoding 설정 했음 cp949 => 근데 파일 형식을 바꾸면서 utf-8로 바뀜
reader = csv.reader(fr, delimiter=',') # 구분자가 ,일 경우 # delimiter는 구분자


for line in reader:
    print(line)

fr.close()
