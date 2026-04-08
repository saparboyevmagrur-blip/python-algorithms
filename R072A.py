N = input().strip() # 1212121212121 => "1212121212121"
even_sum = 0
odd_sum = 0
for index in range(len(N)):
    digit = int(N[index])
    if (index + 1) % 2 == 1:
        odd_sum += digit
    else:
        even_sum += digit

diff = abs(odd_sum - even_sum)
if diff == 0 or diff % 11 == 0:
    print("Yes")
else:
    print("No")