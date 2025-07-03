## Multithreading with Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f'Number: {number}'

numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3]

# create 3 threads using max_workers and try to execute this particular code
# and this will be much more loosely coupled when compared to the previous one,
#  where we have to create each and every threads.

# this will be use all the cores in my CPU
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number,numbers)

for result in results:
    print(result)

# See how fast it is being able to execute even though I gave the time.sleep
# But since we are working with 3 processes