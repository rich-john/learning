# range() doesn't actually do anything by itself. You can't print(range(a, b)) for example
# range(start, end, increment)
# end is not inclusive

total = 0
for number in range(1, 101):
    total += number

print(total)