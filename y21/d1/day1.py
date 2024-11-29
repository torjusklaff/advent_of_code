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
    li = [int(inpu) for inpu in input]
    for i in range(1, len(li)):
        if li[i] > li[i-1]:
            ans1 +=1
    # Part 2
    for i in range(3, len(li)):
        if li[i] + li[i-1] + li[i-2] > li[i-1] + li[i-2] + li[i-3]:
            ans2 +=1

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