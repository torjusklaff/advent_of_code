import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 8

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1

    m = input.splitlines()
    rmax = len(m)
    cmax = len(m[0])
    ants = dict()
    for r in range(rmax):
        for c in range(cmax):
            l = m[r][c]
            if l != '.':
                if l not in ants.keys():
                    ants[l] = [(r,c)]
                else:
                    ants[l].append((r,c))
    antinodes = set()
    for coords in ants.values():
        for f in range(len(coords)-1):
            r1, c1 = coords[f]
            for l in range(f+1,len(coords)):
                r2,c2 = coords[l]
                line = (r1-r2, c1-c2)
                possible_antinodes = [(r1+line[0],c1 + line[1]), (r2-line[0],c2-line[1])]
                for p in possible_antinodes:
                    r,c = p
                    if (0<=r<rmax) and (0<=c<cmax):
                        antinodes.add(p)
    ans1 = len(antinodes)
    # Part 2
    antinodes2 = set()
    for coords in ants.values():
        if len(coords) == 1:
            continue
        for f in range(len(coords)-1):
            r1, c1 = coords[f]
            antinodes2.add((r1,c1))
            for l in range(f+1,len(coords)):
                r2,c2 = coords[l]
                line = (r1-r2, c1-c2)
                i = 0
                while True:
                    i += 1
                    r, c = (r1 - i*line[0], c1 - i*line[1])
                    if (0<=r<rmax) and (0<=c<cmax):
                        antinodes2.add((r,c))
                    else:
                        break
                i = 0
                while True:
                    i += 1
                    r, c = (r2 + i*line[0], c2 + i*line[1])
                    if (0<=r<rmax) and (0<=c<cmax):
                        antinodes2.add((r,c))
                    else:
                        break
    ans2 = len(antinodes2)


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