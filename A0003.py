a = list(map(int, input().split()))

s = sum(a)
min_sum = s - max(a)
max_sum = s - min(a)

print(min_sum, max_sum)

