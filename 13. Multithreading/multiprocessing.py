# What Multiprocessing allows you to do?
# It allows you to create processes that runs in parallel

# When to use multiprocessing ?
# Two reasons: 
# 1. CPU-Bound Tasks - Tasks that are heavy on CPU usage (e.g. Mathematical computation, data processing.)
# 2. Parallel execution - Multiple cores of the CPU

import multiprocessing

import time

def square_number():
    for i in range(5):
        time.sleep(1)
        return (f'square: {i*i}')
    
def cube_number():
    for i in range(5):
        time.sleep(1.5)
        return(f'cube: {i*i*i}')
    
# In order to create two processes, I want to execute this both the code in a seperate process.

# Create my entry point
if __name__ == "__main__":
    
    # Create 2 processes
    p1 = multiprocessing.Process(target= square_number)
    p2 = multiprocessing.Process(target= cube_number)

    t = time.time()
    # start the process
    p1.start()
    p2.start()

    # Wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)

    # This is not going to get executed like threads.
    # It is going to get executed by process and both these processes will be having a separate memory.
