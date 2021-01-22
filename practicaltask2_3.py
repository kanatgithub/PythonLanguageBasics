# 1-ый вариант, через list
Month_list = ['Зима', 'Весна', 'Лето', 'Осень']

while True:
    try:
        month = int(input('Введите порядковый номер месяца: '))
        if month >= 3 and month <= 5:
            print(Month_list[1])
        elif month >= 6 and month <= 8:
            print(Month_list[2])
        elif month >= 9 and month <= 11:
            print(Month_list[3])
        elif month == 12 or month == 1 or month == 2:
            print(Month_list[4])
        else:
            print('Вы ввели некорректные данные, введите числа от 1 до 12')
    except  ValueError:
        print('Вы ввели некорректные данные, введите числа от 1 до 12')

# 2-ый вариант, через dict
month_dictionary = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Осень': [9, 10, 11], 'Лето': [6, 7, 8]}

while True:
    try:
        month = int(input('Введите порядковый номер месяца: '))  # 12
        for key in month_dictionary:  # key = 'Зима'
            if month in month_dictionary[key]:  # 12 в [12, 1, 2]?
                print(key)

    except  ValueError:
        print('Вы ввели некорректные данные, введите числа от 1 до 12')