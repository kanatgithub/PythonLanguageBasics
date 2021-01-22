user_name = input('Напишите Ваше имя: ')
level_glucose = float(input('Введите уровень глюкозы: '))
level_ketones = float(input('Введите уровень кетонов: '))
weight = float(input('Какой ваш вес тела: '))
fat = float(input('Введите процент жира: '))
print(f'Уважаемый {user_name}, Ваш уровень глюкозы: {level_glucose} ммоль и кетонов: {level_ketones} ммоль, '
      f'а также вес составляет: {weight} кг. и % телесного жира: {fat} %.')