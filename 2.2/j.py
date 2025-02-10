num = int(input())

sum1 = (num // 10 % 10) + (num % 10)
sum2 = (num // 100) + (num // 10 % 10)

if sum1 > sum2:
    print(str(sum1) + str(sum2))
else:
    print(str(sum2) + str(sum1))
    