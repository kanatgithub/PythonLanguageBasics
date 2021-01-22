distance = float(input('Сколько километров пробежали в первый день: '))
target_distance = float(input('Какой результат вы хотите достичь: '))
days = 1
while distance < target_distance:
    distance *= 1.1
    days += 1
print(f'На {days}-й день спортсмен достиг результата - не менее {target_distance} км.')

