from functools import cache
import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 11

cache1 = {-1: (-1,-1)}
def get(n):
    if n in cache1:
        return cache1[n]
    if n == 0:
        r = (1, -1)
    else:
        s = str(n)
        l = len(s)
        if l % 2 == 0:
            r = (int(s[:l//2]), int(s[l//2:]))
        else:
            r = (n*2024, -1)
    cache1[n] = r
    return r

cache2 = {}
def get_futures(n, futures):
    if (n, futures) in cache2:
        return cache2[(n,futures)]
    if futures == 1:
        a, b = get(n)
        if b >= 0:
            return 2
        if a >= 0:
            return 1
        return 0
    a, b = get(n)
    l1 = get_futures(a, futures - 1)
    l2 = get_futures(b, futures - 1)
    cache2[(n,futures)] = l1 + l2
    return l1 + l2

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    l =tuple(s_to_int_list(input))
    # Part 1

    for n in l:
        ans1 += get_futures(n, 25)

    # Part 2

    for n in l:
        ans2 += get_futures(n, 75)

    code_end_time = time.time()
    print("Part 1:\n{}".format(ans1))
    print("Part 2:\n{}".format(ans2))
    print("Time: \n{}\n".format(code_end_time - code_start_time))

    return

def main():
    print("\nDay: {}\n".format(day))
    print("Example: ")
    do(readfile(str(filepath)+"/example.txt"))
    print("Input: ")
    do(readfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()