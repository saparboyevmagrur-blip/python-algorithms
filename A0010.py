# import math
# # tepaga qarab yaxlitlash
# print(math.ceil(4.5))
# print(math.ceil(4.1))

# # pastga qarab yaxlitlash
# print(math.floor(4.5))
# print(math.floor(4.9))

# # matematik yaxlitlash
# print(round(4.5))
# print(round(4.4))

import math
a, b, c = map(int, input().split())
print(math.ceil(a / 2) + math.ceil(b / 2) + math.ceil(c / 2))