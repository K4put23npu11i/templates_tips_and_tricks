"""
Created on Sun Nov 22 21:20:00 2020
"""

import sys


def define_progress_bar(bar_width: int):
    bar_str = "[%s]" % (" " * bar_width)
    sys.stdout.write(bar_str)
    sys.stdout.flush()
    sys.stdout.write("\b" * len(bar_str))
    return 0


def update_progress_bar(current_count: int, total_count: int, bar_width: int, divider: int=10):
    progress = current_count / total_count
    bar_str = "[%s] %d%%" % (
            "=" * int(progress*bar_width) + " " * (bar_width - int(progress*bar_width)),
            (progress * 100))
    sys.stdout.write(bar_str)
    sys.stdout.flush()
    sys.stdout.write("\b" * len(bar_str))
    if current_count % divider == 0:
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    all_elements_count = 1000
    prg_bar_width = 40
    
    define_progress_bar(bar_width=prg_bar_width)

    for i in range(0, all_elements_count):
        update_progress_bar(current_count=i, total_count=all_elements_count, bar_width=prg_bar_width)

    print()
    print()
    for i in tqdm(range(0, all_elements_count)):
        time.sleep(0.1)

# https://towardsdatascience.com/learning-to-use-progress-bars-in-python-2dc436de81e5
# import time
# from progress.bar import IncrementalBar
# mylist = [1,2,3,4,5,6,7,8]
# bar = IncrementalBar('Countdown', max = len(mylist))
# for item in mylist:
#    bar.next()
#    time.sleep(1)
# bar.finish()
