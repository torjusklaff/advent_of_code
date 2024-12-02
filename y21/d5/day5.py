import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 5

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    lines = []
    intersections = set()
    for nline in input:
        start, end = nline.split(' -> ')
        if start[0] != end[0] and start[2] != end[2]:
            continue
        start = [int(a) for a in start.split(',')]
        end = [int(a) for a in end.split(',')]
        if start[0] == end[0]:
            if start[1]>=end[1]:
                points = [(start[0],b) for b in range(end[1],start[1]+1)]
            else:
                points = [(start[0],b) for b in range(start[1],end[1]+1)]
        else:
            if start[0]>=end[0]:
                points = [(a,start[1]) for a in range(end[0],start[0]+1)]
            else:
                points = [(a,start[1]) for a in range(start[0],end[0]+1)]
        for line in lines:
            for p in points:
                if p in line:
                    intersections.add(p)
        lines.append(points)

    ans1 = len(intersections)
    # Part 2

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