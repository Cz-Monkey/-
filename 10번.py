try:
    num = int(input('년도 입력 : '))
    num2 = (num//4)*4+4
    print(f'다음 올림픽이 열리는 해는 {num2}년')
except:
    print('정확한 년도를 입력하세요')