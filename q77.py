import timeit

def pow3(n):

    y = 3**n
    return y


elapsed_time = timeit.timeit(lambda: pow3(10000),number=10000)

print(elapsed_time)
