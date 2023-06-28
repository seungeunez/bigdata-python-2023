# 에러/예외 디버깅
# F5를 눌러서 디버깅 F11눌러서 잘 돌아가는지 확인
def add(x, y):
    result = 0
    result = x + y
    return result

def writeText(fname, text):
    try:
        f = open(fname, mode='w', encoding='utf-8')
        f.write(text)
        f.write('\n')
        f.close()
        
        print(f'{fname} 생성 완료')
        
    except Exception as e: #Exception이 모든 에러에 해당해서 UnboundLocalError 이런 자잘자잘한 에러 하나씩 안해줘도됨
        print(f'예외발생{e}')
    # except UnboundLocalError as e:
    #     print(f'예외발생{e}')
    finally: #예외가 발생하든 안하든 무조건 실행되는 부분
        print('파일생성 종료!')
        
    
def divide(x, y):
    result = 0
    try:
        result = x / y
    except Exception as e:
        print(f'예외발생 {e}')

    
    return result

# java와 같은 엔트리포인트
if __name__ == '__main__':
    res = divide(7, 2)
    print(res)
    writeText(fname='예제.txt', text='랄랄라랄랄라')
    

#그냥오류는 문법상의 오류로 빨간줄이 그어져있는데
#예외처리는 실행 중에 발생하는 오류????