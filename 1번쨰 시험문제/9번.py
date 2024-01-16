try:
    num = int(input('년도 입력 : '))
    if num % 4 == 0:
        if num % 100 == 0:
            print('윤년이 아니다')
        else:
            print('윤년입니다')
    else:
        print('윤년이 아닙니다')
except:
    print('년도를 정확히 입력하시오')