n = int(input())
bin_n = input()

dec_n = int(bin_n, 2)

print(n + dec_n)

# Задание
# Ошибка кассового аппарата
# Мы уже помогали магазину с расчётами и формированием чеков, но сегодня кассовый аппарат вместо привычных продавцу десятичных чисел начал выдавать двоичные.
# Техподдержка приедет только завтра, а магазин должен продолжать работать. Надо помочь.

# Формат ввода
# В первой строке записано десятичное число — общая сумма купленных в магазине товаров на данный момент.
# Во второй строке указано двоичное число — сумма за последнюю покупку.

# Формат вывода
# Одно десятичное число — сумма выручки за день с учётом последней покупки.