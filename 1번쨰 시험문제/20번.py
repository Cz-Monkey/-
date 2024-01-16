def large(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        if num1 == num2:
            return num1
        elif num1 == num3:
            return num1
        else:
            return num1
    elif num2 > num3:
        return num2
    else:
        return num3
    
print(large(40,50,70))