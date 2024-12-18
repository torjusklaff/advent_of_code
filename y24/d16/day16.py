import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 16

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    maze = [[c for c in r] for r in input.splitlines()]
    rmax = len(maze)
    cmax = len(maze[0])
    dirs = {'r': (0,1), 'l': (0,-1), 'd':(1,0), 'u':(-1,0)}


    for r in range(rmax):
        for c in range(cmax):
            if maze[r][c] == 'E':
                ends = [(r,c, d) for d in dirs.keys()] 
                maze[r][c] = '.'
                e = (r,c)
            if maze[r][c] == 'S':
                start = (r,c, 'r')
                maze[r][c] = '.'
                s = (r,c)


    nbs = [(r+rd, c+cd) for rd,cd in dirs.values()]

    import math
    dist = {
        (r, c, d): math.inf 
        for c in range(cmax)
        for r in range(rmax)
        for d in dirs.keys()
        if maze[r][c] == '.'  and maze[r+dirs[d][0]][c+dirs[d][1]] == '.'
    }
    ends = [(e[0],e[1], d) for d in dirs.keys() if (e[0],e[1],d) in dist] 

    prev = {
        (r,c,d): None
        for (r,c,d) in dist.keys()
    }
    dist[start] = 0
    prev[start] = []

    q = set([start])

    from heapq import heapify, heappop, heappush 
    q = [(0, start)]
    heapify(q)
    # Part 1
    oppdir = {'d': 'u', 'u':'d', 'r':'l', 'l':'r'}
    while q:
        # mindist = math.inf
        # for coord in q:
        #     if dist[coord] < mindist:
        #         f = coord
        #         mindist = dist[coord]
        # r,c,d = f
        f = heappop(q)
        mindist,(r,c,d) = f
        nbs = [(r+rd, c+cd, dd) for (rd,cd) in dirs.values() for dd in dirs
            if 0 <= r+rd < rmax and 0 <= c+cd < cmax
            and maze[r+rd][c+cd] == '.' and (r+rd,c+cd,dd) in dist]
        for nb in nbs:
                rn, cn, dn = nb
                                
                ndist = mindist + abs(r-rn) + abs(c-cn)
                if dn != d:
                    ndist += 1000
                    if dn == oppdir[d]:
                        ndist += 1000
                if ndist < dist[nb]:
                    dist[nb] = ndist
                    prev[nb] = [(r,c,d)]
                    heappush(q, (ndist, nb))
                elif ndist == dist[nb]:
                    prev[nb].append((r,c,d))

    mindist = math.inf
    for end in ends:
        if dist[end] < mindist:
            mindist = dist[end]
            r_end = end
    ans1 = mindist

    part1_end_time = time.time()

    # Part 2

    curr = r_end
    bestd = set()

    re, ce, de = r_end
    best = set([(re,ce)])
    bestd.add(r_end)
    q = [a for a in prev[r_end]]

    while q:

        curr = q.pop()
        rc, cc, dc = curr
        if curr in bestd:
            continue
        bestd.add(curr)
        best.add((rc,cc))
        currlist = prev[curr]

        if currlist:
            for pr in currlist:
                q.append(pr)

    ans2 = len(best)


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