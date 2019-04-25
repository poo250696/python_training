start = 0
sum = 1
even = 0
while True:
    sum = start + sum
    start = sum - start
    if sum % 2 == 0:
        even += sum
    if sum > 4000000:
        break

# print("Total Sum:", sum)
print("Sum of even values:", even)

