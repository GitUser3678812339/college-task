# 0(n) time complexity
# sum = 0
# for n in range(100000000, 0 -1):
#     sum += n
# print(sum)

def sum_numbers(n, m):
    if n > m:
        max = n
        min = m
    else:
        max = m
        min = n
    foo = ((n+m)*m)/2
    print(foo)

sum_numbers(1, 100000000)