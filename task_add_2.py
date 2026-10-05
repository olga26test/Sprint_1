def digit_root(num):
    if type(num) != int:
        print('Неверный тип данных')
    elif num < 1 or num > 10**7 or type(num) != int:
        print('Неверное число')

    dig_root = 0
    for s in str(num):
        dig_root += int(s)
    num = dig_root
    while dig_root > 10:
        dig_root = 0
        for s in str(num):
            dig_root += int(s)
        num = dig_root
    return dig_root

#проверка функции:
print(digit_root(4851)) #результат = 9
print(digit_root(97569)) #результат = 9
print(digit_root(889987)) #результат = 4