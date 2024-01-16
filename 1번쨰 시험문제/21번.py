def bmi(체중, 키):
    키 = 키 / 100
    bmi = 체중 / (키*키)
    return round(bmi,1)

print(bmi(80,176))