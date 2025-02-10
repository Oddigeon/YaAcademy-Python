n = int(input())
m = int(input())
t = int(input())

minute = (m + t % 60) % 60
hour = ((n + t // 60) + (m + t % 60) // 60) % 24

print(f'{hour:0>2}:{minute:0>2}')

# print(t%60)
# print(t//60)