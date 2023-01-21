from time import perf_counter



f = open('28054-0.txt','r')
t1_start = perf_counter()
text = f.read().upper()
t1_stop = perf_counter()

time_elapsed =  t1_stop - t1_start
print("Time taken for program to execute is ",  time_elapsed)