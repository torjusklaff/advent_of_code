import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 12
dirs = { 'u':(-1,0), 'l': (0,-1), 'r': (0,1), 'd':(1,0)}

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1

    fields = input.splitlines()

    rmax = len(fields)
    cmax = len(fields[0])
    fields = {
        (r, c): [fields[r][c], False]
        for r in range(rmax)
        for c in range(cmax)
    }
    

    for r in range(rmax):
        for c in range(cmax):
            if not fields[(r, c)][1]:
                start = (r,c)
                plot = fields[start][0]
                fields[start][1] = True

                # BFS?
                q = set([start])
                plots = [start]
                # plots[start] = [start]

                circumference = 0
                while q:
                    rr,cc = q.pop()
                    circumference += 4
                    nbs = [(rr+rd, cc+cd) for rd,cd in dirs.values()]
                    for nb in nbs:
                        rb,cb = nb
                        if (0 <= rb < rmax) and (0 <= cb < cmax):
                            if (rb, cb) not in plots:
                                if fields[(rb, cb)][0] == plot:
                                    circumference -= 1
                                    fields[(rb, cb)][1] = True
                                    q.add((rb, cb))
                                    plots.append((rb, cb))
                            else:
                                circumference -= 1
                
                area = len(plots)
                ans1 += area * circumference

                if area == 1:
                    ans2 += 4
                    continue

                plots.sort()
                rs = [p[0] for p in plots]
                cs = [p[1] for p in plots]
                rrmin, rrmax = min(rs), max(rs)
                ccmin, ccmax = min(cs), max(cs)
                plot = [['#' if (rr, cc) in plots else '.' for cc in range(ccmin, ccmax+1)] for rr in range(rrmin, rrmax+1)]
                firstl = True
                firstr = True
                sides = 0
                for rr in range(rrmax - rrmin + 1):

                    new = True
                    levelsl = []
                    for cc in range(ccmax - ccmin + 1):
                        if plot[rr][cc] == '#':
                            if new:
                                new = False
                                levelsl.append(cc)
                                if firstl:
                                    levelsprevl = [cc]
                                    sides += 1

                                    firstl = False
                                if cc not in levelsprevl:
                                    sides += 1
                        else:
                            new = True
                    levelsprevl = levelsl

                    new = True
                    levelsr = []
                    for cc in range(ccmax - ccmin, -1, -1):
                        if plot[rr][cc] == '#':
                            if new:
                                new = False
                                levelsr.append(cc)
                                if firstr:
                                    levelsprevr = [cc]
                                    sides += 1

                                    firstr = False
                                if cc not in levelsprevr:
                                    sides += 1
                        else:
                            new = True
                    levelsprevr = levelsr

                firstl = True
                firstr = True
                for cc in range(ccmax - ccmin + 1):
                    new = True
                    levelsl = []
                    for rr in range(rrmax - rrmin + 1):
                        if plot[rr][cc] == '#':
                            if new:
                                new = False
                                levelsl.append(rr)
                                if firstl:
                                    levelsprevl = [rr]
                                    sides += 1

                                    firstl = False
                                if rr not in levelsprevl:
                                    sides += 1
                        else:
                            new = True
                    levelsprevl = levelsl

                    new = True
                    levelsr = []
                    for rr in range(rrmax - rrmin, -1, -1):
                        if plot[rr][cc] == '#':
                            if new:
                                new = False
                                levelsr.append(rr)
                                if firstr:
                                    levelsprevr = [rr]
                                    sides += 1

                                    firstr = False
                                if rr not in levelsprevr:
                                    sides += 1
                        else:
                            new = True
                    levelsprevr = levelsr

                ans2 += area*sides

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