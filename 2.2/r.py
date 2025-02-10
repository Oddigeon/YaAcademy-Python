a = int(input())
b = int(input())
c = int(input())

max_side = max(a, b, c)
central_min_side = (b ** 2) + (c ** 2) + (a ** 2) - (max_side ** 2)

if (max_side ** 2) < central_min_side:
    print('крайне мала')
elif (max_side ** 2) == central_min_side:
    print('100%')
else:
    print('велика')