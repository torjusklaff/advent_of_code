import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 10


def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    chart = input.splitlines()
    chart = [[int(x) for x in char] for char in chart]
    rmax = len(chart)
    cmax = len(chart[0])

    def paths(r, c, total, vis):
        curr = chart[r][c]
        if curr == 9:
            vis.add((r,c))
            return 1
        nbs = [(r+rn, c+cn) for (rn, cn) in [(1,0),(0,1),(-1,0),(0,-1)]]
        nbs = [(rn,cn) for rn,cn in nbs if (0<=rn<rmax) and (0<=cn<cmax) and chart[rn][cn] == curr + 1]
        totprev = total
        for rn, cn in nbs:
            total += paths(rn,cn,totprev,vis)
        return total
    
    # Part 1

    for r in range(rmax):
        for c in range(cmax):
            if chart[r][c] == 0:
                vis = set()
                a = paths(r, c, 0, vis)
                ans1 += len(vis)
                ans2 += a

    # Part 2


    code_end_time = time.time()
    print("Part 1:\n{}".format(ans1))
    print("Part 2:\n{}".format(ans2))
    print("Time: \n{}\n".format(code_end_time - code_start_time))

    return

def main():
    print("\nDay: {}\n".format(day))
    print("Example: ")
    do(readfile(str(filepath)+"/example.txt"))
    print("Input: ")
    do(readfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()