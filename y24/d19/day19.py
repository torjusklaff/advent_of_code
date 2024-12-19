import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 19

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    patterns, towels = input.split('\n\n')
    patterns = patterns.split(', ')
    patterns = [(pattern, len(pattern)) for pattern in patterns]
    towels = towels.splitlines()

    good_towels = []

    for towel in towels:
        q = [towel]
        while q:
            rem_towel = q.pop()
            if len(rem_towel) == 0:
                ans1 += 1
                good_towels.append(towel)
                break
            for pattern, l in patterns:
                if l <= len(rem_towel) and rem_towel.startswith(pattern):
                    q.append(rem_towel[l:])


    part1_end_time = time.time()
    # Part 2

    cache_remaining = {}
    
    def get_total(towel_strip):
        if len(towel_strip) == 0:
            return 1
        if towel_strip in cache_remaining:
            return cache_remaining[towel_strip]
        tot = 0
        for pattern, l in patterns:
            if l <= len(towel_strip) and towel_strip.startswith(pattern):
                tot += get_total(towel_strip[l:])
        cache_remaining[towel_strip] = tot
        return tot

    for towel in good_towels:
        ans2 += get_total(towel)



    code_end_time = time.time()
    print("Part 1:\n{}".format(ans1))
    print("Part 2:\n{}".format(ans2))
    print("Time Part 1: \n{}\n".format(part1_end_time - code_start_time))
    print("Time Part 2: \n{}\n".format(code_end_time - part1_end_time))
    print("Total time: \n{}\n".format(code_end_time - code_start_time))

    return

def main():
    print("\nDay: {}\n".format(day))
    print("Example: ")
    do(readfile(str(filepath)+"/example.txt"))
    print("Input: ")
    do(readfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()