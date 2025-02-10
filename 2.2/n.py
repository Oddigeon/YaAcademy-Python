N = int(input())

x1 = N // 100
x2 = N // 10 % 10
x3 = N % 10

Max_number = max(x1, x2, x3)
Min_number = min(x1, x2, x3)
Central_number = x1 + x2 + x3 - Max_number - Min_number

if Min_number == 0:
    print(f'{Central_number}{Min_number} {Max_number}{Central_number}')
else:
    print(f'{Min_number}{Central_number} {Max_number}{Central_number}')
    