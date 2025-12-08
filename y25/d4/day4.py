import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 4

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    grid = [[a for a in line] for line in input.splitlines() ]
    rmax = len(grid)
    cmax = len(grid[0])
    grid2 = {}
    remove_rolls = []
    for r in range(rmax):
        for c in range(cmax):
            grid2[(r,c)] = grid[r][c]
    neighbors = [(-1,-1), (-1, 0), (-1,1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for r in range(rmax):
        for c in range(cmax):

            if grid[r][c] == '@':
                nbs = 0
                for rr, cc in neighbors:
                    if (r+rr, c+cc) in grid2.keys() and grid[r+rr][c+cc] == '@':
                        nbs += 1
                    if nbs > 3:
                        break
                if nbs < 4:
                    ans1 += 1
                    remove_rolls.append((r,c))

    

    part1_end_time = time.time()
    removal = True
    ans2 = ans1
    while remove_rolls:
        for r, c in remove_rolls:
            grid[r][c] = '.'
        remove_rolls = []
        for r in range(rmax):
            for c in range(cmax):

                if grid[r][c] == '@':
                    nbs = 0
                    for rr, cc in neighbors:
                        if (r+rr, c+cc) in grid2.keys() and grid[r+rr][c+cc] == '@':
                            nbs += 1
                        if nbs > 3:
                            break
                    if nbs < 4:
                        ans2 += 1
                        remove_rolls.append((r,c))

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