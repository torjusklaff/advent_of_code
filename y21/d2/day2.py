import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 2

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    d = 0
    h = 0
    for line in input:
        a, b = line.split()
        if a == 'forward': h += int(b)
        elif a == 'down': d += int(b)
        else: d -= int(b)
    ans1 = d*h    
    # Part 2
    d = 0
    h = 0
    aim = 0
    for line in input:
        a, b = line.split()
        b = int(b)
        if a == 'forward': 
            h += int(b)
            d += int(b)*aim
        elif a == 'down': aim += int(b)
        else: aim -= int(b)
    ans2 = d*h   

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