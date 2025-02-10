abcd = int(input())

a = abcd // 1000
b = abcd // 100 % 10
c = abcd // 10 % 10
d = abcd % 10

if a == d and b == c:
    print('YES')
else:
    print('NO')