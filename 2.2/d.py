p = int(input())
v = int(input())
t = int(input())

first = max(p, v, t)
last = min(p, v, t)

if last < p < first:
    middle = p
elif last < v < first:
    middle = v
else:
    middle = t

print(f'1. {first}')
print(f'2. {middle}')
print(f'3. {last}')


