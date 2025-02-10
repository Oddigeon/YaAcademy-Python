z1 = int(input())
z2 = int(input())

x1 = z1 // 10
x2 = z1 % 10
x3 = z2 // 10
x4 = z2 % 10

Min_number = min(x1, x2, x3, x4)
Max_number = max(x1, x2, x3, x4)
Central_number = (x1 + x2 + x3 + x4 - Max_number - Min_number) % 10

print(f'{Max_number}{Central_number}{Min_number}')