name = input()
price = int(input())
weight = int(input())
money = int(input())

total = price * weight
ch = money % total

print('Чек')
print(f'{name} - {weight}кг - {price}руб/кг')
print(f'Итого: {total}руб')
print(f'Внесено: {money}руб')
print(f'Сдача: {ch}руб')