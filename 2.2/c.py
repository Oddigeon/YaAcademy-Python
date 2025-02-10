p = int(input())
v = int(input())
t = int(input())

if p > v and p > t:
    print('Петя')
elif v > p and v > t:
    print('Вася')
else:
    print('Толя')