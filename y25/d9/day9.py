import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time
import math
day = 9

def do(input, example):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    points = []
    largest = 0
    areas = []
    for line in input.splitlines():
        points.append(tuple(s_to_int_list(line,',')))
    for i in range(len(points)):
        a,b = points[i]
        for aa,bb in points[i+2:]:
            area = (abs(a-aa)+1)*(abs(b-bb)+1)
            areas.append(area)
            if area > largest:
                largest = area
    ans1 = largest
    unareas = set(areas)
    part1_end_time = time.time()
    # Part 2
    dirs = {'r': (0,1), 'l': (0,-1), 'd':(1,0), 'u':(-1,0)}
    dir = 'r'
    x,y = points[0]
    x0, y0 = points[-1]
    if x - x0 < 0:
        dir = 'd'
    elif x -x0 > 0:
        dir = 'u'
    elif y - y0 < 0:
        dir = 'l'
    else:
        dir = 'r'
    cw = 0
    for i in range(1,len(points)):
        x, y = points[i]
        x0, y0 = points[i-1]
        prevdir = dir
        if x - x0 < 0:
            dir = 'd'
        elif x -x0 > 0:
            dir = 'u'
        elif y - y0 < 0:
            dir = 'l'
        else:
            dir = 'r'
        if dir == prevdir:
            continue
        if dir == 'u':
            if prevdir == 'r':
                cw -= 1
            else:
                cw += 1
        elif dir == 'd':
            if prevdir == 'l':
                cw -= 1
            else:
                cw += 1
        elif dir == 'r':
            if prevdir == 'u':
                cw += 1
            else:
                cw -= 1
        else:
            if prevdir == 'd':
                cw += 1
            else:
                cw -= 1
    largest = 0
    if not example:
        end = points.index((94737,50322))
        x, y = points[end]
        for x1, y1 in points:
            if x1 < x:
                maxy = y1
                break
        for point in points[:end]:
            x1, y1 = point
            area = (abs(x-x1)+1)*(abs(y-y1)+1)
            if area > largest and y1 < maxy:
                largest = area
        start = points.index((94737,48449))
        x, y = points[start]
        for x1,y1 in points[-1:0:-1]:
            if x1 < x:
                miny = y1
                break
        for point in points[start+1:]:
            x1, y1 = point
            area = (abs(x-x1)+1)*(abs(y-y1)+1)
            if area > largest and y1 > miny:
                largest = area

    ans2 = largest


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
    do(readfile(str(filepath)+"/example.txt"), True)
    print("Input: ")
    do(readfile(str(filepath)+"/input.txt"), False)

if __name__=="__main__":
    main()