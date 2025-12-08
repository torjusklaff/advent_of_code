import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 1

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    code = 50
    ops = input.splitlines()
    for op in ops:
        prevcode = code
        numturn = int(op[1::])
        numfullrots = 0
        if numturn >= 100:
            numfullrots = numturn//100
            ans2 += numfullrots
        if op[0] == "L":
            code = code - numturn
            code = code % 100
            if code >= prevcode and prevcode != 0 and code != 0:
                ans2 += 1
        else:
            code = code + numturn
            code = code % 100

            if code <= prevcode and prevcode != 0 and code != 0:
                ans2 += 1

        if code == 0:
            ans1 += 1
            ans2 += 1
        
    part1_end_time = time.time()
    # Part 2


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