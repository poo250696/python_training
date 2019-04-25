# 0 + 1 => 1
# 1 + 2 => 3
# 2 + 3 => 5
# 3 + 4 => 7

start = 0
# second = 1
sum = 0
for i in range(1, 10):
    sum = start + i
    start = i
    print(sum)

