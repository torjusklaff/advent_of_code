import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 15

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    warehouse, dirs = input.split('\n\n')

    warehouse = [[c for c in r] for r in warehouse.splitlines()]
    rmax = len(warehouse)
    cmax = len(warehouse[0])
    w2 = []
    for r in warehouse:
        s = ''
        for c in r:
            if c == '#':
                s += '##'
            elif c == 'O':
                s += '[]'
            elif c == '.':
                s += '..'
            else:
                s += '@.'
        w2.append([x for x in s])
    rmax2 = (len(w2))
    cmax2 = (len(w2[0]))
    start = (-1,-1)
    s2 = (-1,-1)
    for r in range(rmax):
        for c in range(cmax):
            if warehouse[r][c] == '@':
                start = (r,c)
                warehouse[r][c] = '.'
                break
        if start != (-1,-1):
            break
    for r in range(rmax2):
        for c in range(cmax2):
            if w2[r][c] == '@':
                s2 = (r,c)
                w2[r][c] = '.'
                break
        if s2 != (-1,-1):
            break

    directions = ''
    for d in dirs.splitlines():
        directions += d
    dirs = {'>': (0,1), 'v':(1,0), '<':(0,-1), '^':(-1,0)}
    

    pos = start
    for d in directions:
        r, c = pos
        rd, cd = dirs[d]
        rr, cc = r + rd, c + cd

        if warehouse[rr][cc] == '.':
            pos = (rr,cc)
        elif warehouse[rr][cc] == '#':
            continue
        else:
            if d == '>':
                for cn in range(cc, cmax):
                    if warehouse[r][cn] == '.':
                        warehouse[r][cn] = 'O'
                        warehouse[rr][cc] = '.'
                        pos = (rr,cc)
                        break
                    elif warehouse[r][cn] == '#':
                        break
            elif d == '<':
                for cn in range(cc, -1, -1):
                    if warehouse[r][cn] == '.':
                        warehouse[r][cn] = 'O'
                        warehouse[rr][cc] = '.'
                        pos = (rr,cc)
                        break
                    elif warehouse[r][cn] == '#':
                        break
            elif d == 'v':
                for rn in range(rr, rmax):
                    if warehouse[rn][c] == '.':
                        warehouse[rn][c] = 'O'
                        warehouse[rr][cc] = '.'
                        pos = (rr,cc)
                        break
                    elif warehouse[rn][c] == '#':
                        break
            elif d == '^':
                for rn in range(rr, -1, -1):
                    if warehouse[rn][c] == '.':
                        warehouse[rn][c] = 'O'
                        warehouse[rr][cc] = '.'
                        pos = (rr,cc)
                        break
                    elif warehouse[rn][c] == '#':
                        break


    for r in range(rmax):
        for c in range(cmax):
            if warehouse[r][c] == 'O':
                ans1 += 100 * r + c



    # Part 2

    pos = s2

    def search(r,c, dir, current):
        ncurr = w2[r][c]
        if ncurr == current:
            return search(r + dir,c, dir, current)
        elif ncurr == '#':
            return False
        elif ncurr == '.':
            return True
        else:
            if current == '[':
                return search(r + dir, c, dir, ']') and search(r + dir, c - 1, dir, current)
            else:
                return search(r + dir, c, dir, '[') and search(r + dir, c + 1, dir, current)
            
    def move(r,c, dir, current):
        ncurr = w2[r][c]
        if ncurr == current:
             move(r + dir,c, dir, current)
        elif ncurr == '.':
            w2[r][c] = current
        else:
            if current == '[':
                w2[r][c] = current
                w2[r][c - 1] = '.'
                move(r + dir, c, dir, ']')  
                move(r + dir, c - 1, dir, current)
            else:
                w2[r][c] = current
                w2[r][c + 1] = '.'
                move(r + dir, c, dir, '[')  
                move(r + dir, c + 1, dir, current)


    for d in directions:
        r, c = pos
        rd, cd = dirs[d]
        rr, cc = r + rd, c + cd

        if w2[rr][cc] == '.':
            pos = (rr,cc)
        elif w2[rr][cc] == '#':
            continue
        else:
            if d == '>':
                for cn in range(cc, cmax2):
                    if w2[r][cn] == '.':
                        for cdn in range(1, cn-cc+1):
                            if cdn%2 == 1:
                                w2[r][cc+cdn] = '['
                            else:
                                w2[r][cc+cdn] = ']'

                        w2[rr][cc] = '.'
                        pos = (rr,cc)
                        break
                    elif w2[r][cn] == '#':
                        break
            elif d == '<':
                for cn in range(cc, -1, -1):
                    if w2[r][cn] == '.':
                        for cdn in range(1, cc-cn+1):
                            if cdn%2 == 1:
                                w2[r][cc-cdn] = ']'
                            else:
                                w2[r][cc-cdn] = '['
                        w2[rr][cc] = '.'
                        
                        pos = (rr,cc)
                        break
                    elif w2[r][cn] == '#':
                        break
            elif d in 'v^':
                current = w2[rr][cc]
                if current == ']':
                    other = '['
                    cdir = -1
                else:
                    other = ']'
                    cdir = 1
                if d == 'v':
                    rdir = 1
                else:
                    rdir = -1

                fits = search(rr, cc, rdir, current) and search(rr, cc + cdir, rdir, other)
                if fits:
                    move(rr,cc, rdir, current)
                    move(rr,cc+cdir, rdir, other)

                    w2[rr][cc] = '.'
                    w2[rr][cc+cdir] = '.'
                    pos = (rr,cc)


    for r in range(rmax2):
        for c in range(cmax2):
            if w2[r][c] == '[':
                ans2 += 100 * r + c

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