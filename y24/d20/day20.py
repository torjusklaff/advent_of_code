import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 20

def do(input, example=False):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    maze = [[c for c in r] for r in input.splitlines()]
    rmax = len(maze)
    cmax = len(maze[0])
    dirs = {'r': (0,1), 'l': (0,-1), 'd':(1,0), 'u':(-1,0)}

    num_opens = 0
    for r in range(rmax):
        for c in range(cmax):
            if maze[r][c] == 'E':
                ends = [(r,c, d) for d in dirs.keys()] 
                maze[r][c] = '.'
                end = (r,c)
                num_opens += 1
            elif maze[r][c] == 'S':
                start = (r,c, 'r')
                maze[r][c] = '.'
                start = (r,c)
                num_opens += 1
            elif maze[r][c] == '.':
                num_opens += 1


    q = [(str(start), start)]
    visited = set()

    while q:
        path, last = q.pop(0)
        r, c = last
        if last == end:
            path_len = len(visited)
            break
        nbs = [(r+rd, c+cd) for (rd,cd) in dirs.values()
            if 0 <= r+rd < rmax and 0 <= c+cd < cmax
            and maze[r+rd][c+cd] == '.']
        for nb in nbs:
            if nb in visited or nb == start:
                continue
            p = path + ':' + str(nb)
            visited.add(nb)
            q.append((p, nb))
    path = [eval(s) for s in path.split(':')]
    
    dists = dict()

    for i in range(len(path)):
        dists[path[i]] = i

    mindist = 100
    if example:
        mindist = 2

    for p in path:
        r, c = p
        nnbs = [(r+2*rd, c+2*cd) for (rd,cd) in dirs.values()
            if 0 <= r+2*rd < rmax and 0 <= c+2*cd < cmax
            and maze[r+2*rd][c+2*cd] == '.']
        for nb in nnbs:
            if dists[nb] - dists[p] - 2 >= mindist:
                ans1 += 1


    part1_end_time = time.time()
    # Part 2
    if example:
        mindist = 50
    for p in range(len(path) - mindist):
        curr = path[p]
        r, c = curr
        for pp in path[p+mindist:]:
            rr, cc = pp
            dist = abs(r-rr) + abs(c-cc)
            if dist <= 20 and dists[pp] - dists[curr] - dist >= mindist:
                ans2 += 1




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
    do(readfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()