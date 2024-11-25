n = int(input('Введите число из первого поля для получения пароля: '))
def get_password(number):
    password=''
    if n > 20:
        print('Вы ввели неверное число')
        return password
    for i in range(1, number):
        for j in range(1, number):
            if j <= i:
                continue
            if number % (i+j) == 0:
                password+=str(i)+str(j)
    return password
result = get_password(n)
print(result)