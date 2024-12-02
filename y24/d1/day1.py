import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 1

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    l1 = []
    l2 = []
    for line in input:
        a, b = s_to_int_list(line)
        l1.append(a)
        l2.append(b)
    l1.sort()
    l2.sort()
    ans1 = sum([abs(a-b) for a,b in zip(l1,l2)])

    # Part 2
    ans2 = sum([a*l2.count(a) for a in l1])

    code_end_time = time.time()
    print("Part 1: ")
    print(ans1)
    print("Part 2: ")
    print(ans2)
    print("Time: ", code_end_time - code_start_time)
    return

def main():
    print()
    print("Day: ", day)
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print()
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))
    print()

if __name__=="__main__":
    main()