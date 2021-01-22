seconds = int(input('Введите время в секундах: '))
hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
rest_of_seconds = seconds - (hours * 3600 + minutes * 60)
print(f'Время в формате чч:мм:сс / {hours}:{minutes}:{rest_of_seconds}')



