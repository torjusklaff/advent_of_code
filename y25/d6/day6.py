import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 6

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    equations = []
    for line in input.splitlines():
        try:
            equations.append(s_to_int_list(line))
        except ValueError:
            equations.append(line.split())
    for i in range(len(equations[0])):
        if equations[-1][i] == '+':
            s = 0
            for j in range(len(equations)-1):
                s += equations[j][i]
        else:
            s = 1
            for j in range(len(equations)-1):
                s = s*equations[j][i]
        ans1 += s
    part1_end_time = time.time()
    # Part 2
    grid = []
    lines = input.splitlines()
    l = []

    for j in range(len(lines[0]) - 1, -1, -1):
        s = ''
        for i in range(len(lines) - 1):
            if lines[i][j] != ' ':
                s += lines[i][j]
        if s == '':
            
            l.append(lines[-1][j+1])
            grid.append(l)
            l = []
        else:
            l.append(s)
    l.append(lines[-1][0])
    grid.append(l)
    for g in grid:
        if g[-1] == '+':
            s = 0
            for j in range(len(g)-1):
                s += int(g[j])
        else:
            s = 1
            for j in range(len(g)-1):
                s = s*int(g[j])
        ans2 += s


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