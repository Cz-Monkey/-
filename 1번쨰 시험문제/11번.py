try:
    num = int(input('숫자 입력 : '))
    if num % 4 == 0:
        if num % 100 == 0:
            num = (num // 4) * 4 + 4
            print(f'다음 윤년은 {num}년 입니다')
        else:
            print(f'{num}년은 윤년입니다')
    elif num % 4 != 0:
        num = (num // 4) * 4 + 4
        print(f'다음 윤년은 {num}년 입니다')
except:
    print('정확한 년도를 입력하시오')