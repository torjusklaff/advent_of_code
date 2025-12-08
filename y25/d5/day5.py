import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 5

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    
    ranges, ingredients = input.split('\n\n')
    rs = []
    for ra in ranges.splitlines():
        s, e = ra.split('-')
        rs.append((int(s), int(e)))
    for ing in ingredients.splitlines():
        for ra in rs:
            s, e = ra
            if int(ing) in range(s,e+1):
                ans1 += 1
                break

    part1_end_time = time.time()
    # Part 2
    l = 559215810479919
    h = 0
    skip_index = []
    pre_ans = 0
    # for s,e in rs:
    #     pre_ans += 1+e-s
    collections = []
    for i in range(len(rs)):
        s, e = rs[i]
        if s < l:
            l = s
        if e > h:
            h = e
    ranges = [rs[0]]
    completed_ranges = set()
    while rs:
        new_ranges = []

        s, e = rs.pop(0)
        for ss, ee in rs:
            if s <= ss and e >= ee:
                new_ranges.append((s,e))
            elif s < ss and e >= ss:
                new_ranges.append((s,ee))
            elif e > ee and s <= ee:
                new_ranges.append((ss,e))
            elif s >= ss and e <= ee:
                new_ranges.append((ss,ee))
                s = 0
                e = -1
            else:
                new_ranges.append((ss,ee))

        if new_ranges != rs:
            rs = new_ranges
        else: 
            completed_ranges.add((s,e))

    for s, e in completed_ranges:
        ans2 += 1+e-s


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