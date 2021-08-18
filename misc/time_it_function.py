"""
Created on Wed Mar 11 14:31:11 2020
"""

import time
import functools


def time_it(i_function):
    @functools.wraps(i_function)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()

        value = i_function(*args, **kwargs)

        end = time.perf_counter()
        run_time = end - start
        print(f"Run function {i_function.__name__!r} in {run_time:.4f} seconds")

        return value

    return wrapper_timer


def run1():
    print("Run1")
    print("wait 2 secs")
    time.sleep(2)
    print("Done")
    

@time_it
def run2():
    print("Run2")
    print("wait 2 secs")
    time.sleep(2)
    print("Done")


if __name__ == '__main__':
    run1()
    run2()
