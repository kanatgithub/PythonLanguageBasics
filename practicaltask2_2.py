my_data_str = input('Введите через пробел элементы для формирования списка: ')
my_data = my_data_str.split()
print(my_data)
for i in range(0,len(my_data)-1,2):
    my_data[i], my_data[i+1] = my_data[i+1], my_data[i]
print(my_data)
