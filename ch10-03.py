def count_down(n):
    if n <= 0:
        print("countdown ended")
        return
    print(n)
    count_down(n - 1) # count_down callback

count_down(5)