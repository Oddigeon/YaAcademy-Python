abcd = int(input())

n1 = str(abcd // 1000)
n2 = str(abcd // 100 % 10)
n3 = str(abcd // 10 % 10)
n4 = str(abcd % 10)

badc = n2 + n1 + n4 + n3

print(badc)