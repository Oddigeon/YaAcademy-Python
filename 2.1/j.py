name = input()
num = int(input())

num_g = num // 100
num_bed = num // 10 % 10
num_child = num % 10

print(f'Группа №{num_g}.')
print(f'{num_child}. {name}.')
print(f'Шкафчик: {num}.')
print(f'Кроватка: {num_bed}.')