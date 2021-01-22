proceeds = float(input('Введите значение выручки: '))
costs = float(input('Введите значение издержки фирмы: '))
net_profit = float(proceeds - costs) #'Чистая прибыль'
profitability = float(net_profit / proceeds) #'Рентабильность'
if proceeds > costs:
    print('Прибыль')
    print(f'{profitability:.2f}')
    staffing = int(input('Укажите численность сотрудников: '))
    net_profit_per_employee = net_profit / staffing
    print(f'Чистая прибыль фирмы на одного сотрулника составляет: {net_profit_per_employee:.2f}')
else:
    print("Убыток")
