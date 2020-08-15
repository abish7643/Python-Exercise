# Write a recursive function to find nth fibonacci term with Memoization


print("------Space Optimized Way-------")

"""
1
1 = N - 2 Number
2 = N - 1 Number
3 = Number (N - 1) + (N - 2)
4
5

"""

import time
start_time = time.time()

n = 5
number = 0
prev_number = 0
prev_prev_number = 0

for i in range(n):
    if i ==0:
        number = 1
    elif i == 1:
        number = 1
        prev_prev_number = 1
        prev_number = 1
    else:
        number = prev_prev_number + prev_number
        prev_prev_number = prev_number
        prev_number = number
    print("-----{}-----".format(number))


print("--- %s seconds ---" % (time.time() - start_time))



print("---------Recursive Fn Way----------")

start_time_1 = time.time()

def FibonacciSeries(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return FibonacciSeries(n-1) + FibonacciSeries(n-2)

for i in range(5):
    print(FibonacciSeries(i))

print("--- %s seconds ---" % (time.time() - start_time_1))


