n = int(input('Введите целое положительное число: '))
a = n % 10
n = n // 10
while n != 0:
    b = n % 10
    if b > a:
        a = b
    n = n // 10
print(a)

#num_user
