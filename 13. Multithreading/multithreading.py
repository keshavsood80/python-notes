# Multithreading
# When to use Multi Threading

# For this there are two important reasons: 

# 1. I/O bound tasks: Tasks that spend more time waiting for I/O operations 
# (eg. File Operation, Network requests)

# 2. Concurrent execution: When you want to improve the throughput of your application
#  by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'Number:{i}')

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f'letter: {letter}')
# when this is actually sleeping, we are just waiting for this particular thread to
#  become active or complete that particular i/o operation and come back to this particular code.

# I should allow second code to get executed

# So if anything sleeps over here in this particular print_numbers() function, i should allow
# second function print_letter() to continue

# One thread will be responsible in running this entire code, and the other thread will be 
# responsible for running second code.
    
# create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)
# One of the thread will get sleep,but the other thread will concurrently getting executed.

t = time.time()
# start the thread
t1.start()
t2.start()

# Wait for the threads to complete
t1.join()
t2.join()
# both the execution happens, then both this particular threads will be joined back to the main thread.


finished_time = time.time() - t
print(finished_time)