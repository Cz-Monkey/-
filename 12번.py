try:
    num = int(input('달을 입력하시오 : '))
    if num == 2:
        print(f'{num}월은 28일까지입니다')
    elif num in (4,6,9,11):
        print(f'{num}월은 30일까지입니다')
    elif num in (1,3,5,7,8,10,12):
        print(f'{num}월은 31일까지입니다')
except:
    print('정확한 날짜를 입력하시오')