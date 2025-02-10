nameproduct = input()
priceproduct = int(input())
vesproduct = int(input())
moneypayment = int(input())

moneybuy = priceproduct * vesproduct
moneysdacha = moneypayment - moneybuy
moneysdacha2 = int(moneysdacha)

print(f'{"Чек":=^35}')
print(f'{"Товар:":<10}{nameproduct:>25}')
print(f'{"Цена:":<10}{f"{vesproduct}кг * {priceproduct}руб/кг":>25}')
print(f'{"Итого:":<10}{str(moneybuy) + "руб":>25}')
print(f'{"Внесено:":<10}{str(moneypayment) + "руб":>25}')
print(f'{"Сдача:":<10}{str(moneysdacha2) + "руб":>25}')
print('=' * 35)

# Украшение чека
# Давайте приведём в порядок чек, который печатали ранее.
# Все строки должны быть длиной в 35 символов.

# Формат ввода
# Название товара;
# цена товара;
# вес товара;
# количество денег у пользователя.
# Формат вывода
# Красивый чек в формате:

# ================Чек================
# Товар:                    <продукт>
# Цена:     <число>кг * <число>руб/кг
# Итого:                   <число>руб
# Внесено:                 <число>руб
# Сдача:                   <число>руб
# ===================================


# Мой вариант не подошел по стандарту

# product = input()
# price = int(input())
# weight = int(input())
# money = int(input())

# final_price = weight * price
# st = money - final_price

# # print('=' * 16, f'{'Чек':=<19}', sep='')
# print(f'{"Чек":=^35}')
# print(f'Товар:{product:>29}')
# print(f'Цена:{weight:>16} кг * {price} руб/кг')
# print(f'Итого:{final_price:>25} руб')
# print(f'Внесено:{money:>23} руб')
# print(f'Сдача:{st:>25} руб')
# print('=' * 35) 



