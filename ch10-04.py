def arr_sum(arr,n):
    if n <= 0:
        return 0
    else:
        return arr[n-1] + arr_sum(arr, n-1) #arr_sum callback

foo = [1, 2, 3, 4, 5]
arr_sum(foo, len(foo))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # fibonacci callback

print(fibonacci(5))

