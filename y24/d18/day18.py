import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 18

def do(input, example=False):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1

    rmax = 71
    cmax = 71
    if example:
        rmax = 7
        cmax = 7
    maze = [['.' for c in range(cmax)]for r in range(rmax)]

    coords = input.splitlines()
    if example:
        coords2 = coords
        coords = coords[:12]
    for coord in coords[:1024]:
        cc,rr = s_to_pos_list(coord)
        maze[int(rr)][int(cc)] = '#'

    start = (0,0)
    end = (70,70)
    if example:
        end = (6,6)


    dirs = {'r': (0,1), 'l': (0,-1), 'd':(1,0), 'u':(-1,0)}

    import math
    dist = {
        (r, c): math.inf 
        for c in range(cmax)
        for r in range(rmax)
        if maze[r][c] == '.'
    }
    dist[start] = 0

    # q = set([start])
    # while q:
    #     mindist = math.inf
    #     for coord in q:
    #         if dist[coord] < mindist:
    #             f = coord
    #             mindist = dist[coord]
    #     r,c = f
    #     q.remove(f)
    #     if f == end:
    #         break

    #     nbs = [(r+rd, c+cd) for (rd,cd) in dirs.values()
    #         if 0 <= r+rd < rmax and 0 <= c+cd < cmax
    #         and maze[r+rd][c+cd] == '.' and (r+rd,c+cd) in dist]
        
    #     for nb in nbs:
    #         ndist = mindist + 1
    #         if ndist < dist[nb]:
    #             dist[nb] = ndist
    #             q.add(nb)


    # ans1 = dist[end]
    # part1_end_time = time.time()

    q = [(str(start), start)]
    visited = set()

    while q:
        path, last = q.pop(0)
        r, c = last
        if last == end:
            ans1 = len(path.split(':')) - 1
            break
        nbs = [(r+rd, c+cd) for (rd,cd) in dirs.values()
            if 0 <= r+rd < rmax and 0 <= c+cd < cmax
            and maze[r+rd][c+cd] == '.']
        for nb in nbs:
            if nb in visited:
                continue
            p = path + ':' + str(nb)
            visited.add(nb)
            q.append((p, nb))

    part1_end_time = time.time()
    # Part 2

    i_min = 1024
    if example:
        i_min = 12
        coords = coords2

    found = False
    #for i in range(i_min, len(coords)):
    true_coords = []
    for coord in coords:
        cc, rr = s_to_int_list(coord,',')
        true_coords.append((rr,cc))
    pos = true_coords[i_min:]
    filled = set(true_coords[:i_min])
    while not found:
        i = len(pos)//2
        visited = set()
        n_filled = set(pos[:i])
        q = [(str(start), start)]
        while q:
            path, last = q.pop()
            r, c = last
            if last == end:
                break
            nbs = [(r+rd, c+cd) for (rd,cd) in dirs.values()
                if 0 <= r+rd < rmax and 0 <= c+cd < cmax]
            for nb in nbs:
                if nb in visited:
                    continue
                if nb in n_filled or nb in filled:
                    continue
                p = path + ':' + str(nb)
                visited.add(nb)
                q.append((p, nb))
        if end not in visited:
            pos = pos[:i]
        else:
            i_min += i
            filled = set(true_coords[:i_min])
            pos = pos[i:]
        if len(pos) == 1:
            ans2 = str(pos[0][1]) + ',' + str(pos[0][0])
            break

    # for i in range(i_min, len(coords)):
    #     cc,rr = s_to_pos_list(coords[i])

    #     maze[int(rr)][int(cc)] = '#'
    #     dist = {
    #         (r, c): math.inf 
    #         for c in range(cmax)
    #         for r in range(rmax)
    #         if maze[r][c] == '.'
    #     }
    #     dist[start] = 0

    #     q = set([start])
    #     while q:
    #         mindist = math.inf
    #         for coord in q:
    #             if dist[coord] < mindist:
    #                 f = coord
    #                 mindist = dist[coord]
    #         r,c = f
    #         try:
    #             q.remove(f)
    #         except Exception:
    #             ans2 = coords[i]
    #             found = True
    #             break
    #         if f == end:
    #             break

    #         nbs = [(r+rd, c+cd) for (rd,cd) in dirs.values()
    #             if 0 <= r+rd < rmax and 0 <= c+cd < cmax
    #             and maze[r+rd][c+cd] == '.' and (r+rd,c+cd) in dist]
            
    #         for nb in nbs:
    #             ndist = mindist + 1
    #             if ndist < dist[nb]:
    #                 dist[nb] = ndist
    #                 q.add(nb)

    #     if dist[end] == math.inf:
    #         ans2 = coords[i]
    #         break
    #     if found:
    #         break
    


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