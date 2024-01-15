def 문자열(목록):
    max = 0
    result = ''
    for 가장긴 in 목록:
        if len(가장긴) > max:
            max = len(가장긴)
            result = 가장긴
    return result

print(문자열(['우리나라좋은나라', 'python', 'java']))