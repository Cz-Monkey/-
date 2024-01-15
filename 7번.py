try:
    num = int(input('숫자입력 : '))
    if num % 2 == 0:
        print(f'{num}는 짝수입니다')
    else:
        print(f'{num}는 홀수입니다')
except:
    print('숫자를 입력하세요')