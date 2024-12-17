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

    q = set([d for d in dist.keys()])

    # Part 1
    oppdir = {'d': 'u', 'u':'d', 'r':'l', 'l':'r'}
    while q:
        mindist = math.inf
        for coord in q:
            if dist[coord] < mindist:
                f = coord
                mindist = dist[coord]
        r,c,d = f
        q.remove(f)
        nbs = [(r+rd, c+cd, dd) for (rd,cd) in dirs.values() for dd in dirs
            if 0 <= r+rd < rmax and 0 <= c+cd < cmax
            and maze[r+rd][c+cd] == '.' and (r+rd,c+cd,dd) in dist and (r+rd,c+cd,dd) in q]
        for nb in nbs:
                rn, cn, dn = nb
                                
                ndist = mindist + abs(r-rn) + abs(c-cn)
                if dn != d:
                    ndist += 1000
                    if dn == oppdir[d]:
                        ndist += 1000
                if ndist < dist[nb]:
                    dist[nb] = ndist
                    prev[nb] = [f]
                elif ndist == dist[nb]:
                    prev[nb].append(f)

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


    # q = [(set([s]),s, 'r', 0)]
    # found_p = []
    # mindist = math.inf
    # minlen = math.inf
    # invdir = {(1,0): 'd', (0,1): 'r', (-1,0): 'u', (0, -1): 'l'}

    # while q:
    #     path, last, dir, dist = q[0]
    #     q.remove((path, last, dir, dist))
    #     path.add(last)
    #     if dist > mindist:
    #         continue
    #     rr, cc = last
    #     if (rr,cc) == e:
    #         if dist < mindist:
    #             mindist = dist
    #             found_p = [[p for p in path]]
    #         else:
    #             found_p.append([p for p in path])

    #         continue
        
    #     nbs = [(rr+rd, cc+cd) for rd,cd in dirs.values()]
    #     for nb in nbs:
    #         rb,cb = nb
    #         if (0 <= rb < rmax) and (0 <= cb < cmax) and maze[rb][cb] == '.' and (rb,cb) not in path:

    #             if (rr - rb, cc - cb ) != dirs[dir]:
    #                 distn = dist + 1001
    #                 dirn = invdir[(rr - rb, cc - cb)]
    #             else:
    #                 distn = dist + 1
    #                 dirn = invdir[(rr - rb, cc - cb)]

    #             p = set(path)
    #             q.append((p, (rb, cb), dirn, distn))

        
    # ans1 = mindist

    # best = set()

    # for path in found_p:
    #     for p in path:
    #         best.add(p)
    
    # ans2 = len(best)


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