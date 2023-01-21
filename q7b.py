import timeit


def pow3(n):

    cubic_list = [3**x for x in range(n)]
    return cubic_list

elapsed_time = timeit.timeit(lambda: pow3(1000),number=1000)

print(elapsed_time)