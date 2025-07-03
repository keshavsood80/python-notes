'''
Real world Example: Multiprocessing for CPU Bound Tasks

Scenerio : Factorial calculation specially for large no.,
involve significant computational work.
Multiprocessing can be used to distribute the workload across multiple CPU cores,
improving performances.

'''

import multiprocessing
import math
import time
import sys

# Increase the maximum no. of digits for integer conversion
sys.set_int_max_str_digits(100000)

# function to compute factorials of a given number
def computer_factorial(number):
    print(f'Computing factorial of {number}')
    result = math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result

if __name__ == '__main__':
    numbers = [50,60,888]

    start_time=time.time()

    # create a pool of worker processes
    # with the help of this particular tool we will be able to map our function with this all no.s
    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial,numbers)
    
    end_time = time.time()

    print(f'Results: {results}')
    print(f'Time Taken: {end_time} - {start_time} seconds')