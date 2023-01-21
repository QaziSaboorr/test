import timeit


def instances(n):
    for x in range(n):
        pow2(n)
   

def pow2(n):
    


    y = 2**n
    return y

n = int(input("Please enter a number to compute power of 2: "))
result = pow2(n)
elapsed_time = timeit.timeit(lambda: instances(n),number=1)
print(elapsed_time)
