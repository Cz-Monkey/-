try:
    num = int(input('년도 입력 :'))
    if num % 4 == 2:
        print('월드컵이 열리는 해입니다')
    elif num % 4 == 0:
        print('올림픽이 열리는 해입니다')
    else:
        print('월드컵도 올림픽도 열리지 않는 해입니다')
except:
    print('년도를 입력하시오')