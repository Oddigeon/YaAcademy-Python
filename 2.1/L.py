n = int(input())
m = int(input())

sum = str((n // 100 + m // 100) % 10) + str((n // 10 % 10 + m // 10 % 10) % 10) + str((n % 10 + m % 10) % 10)

print(sum)