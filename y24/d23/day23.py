import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 23

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1

    connections = {}

    for cable in input.splitlines():
        a,b = cable.split('-')
        if a not in connections:
            connections[a] = set([b])
        else:
            connections[a].add(b)
        if b not in connections:
            connections[b] = set([a])
        else:
            connections[b].add(a)
            
    triplets = set()
    for pc in connections:
        for nb in connections[pc]:
            for third in connections[nb]:
                if third in connections[pc] and (pc.startswith('t') or nb.startswith('t') or third.startswith('t')):
                    a = sorted([pc,nb,third])
                    triplets.add(tuple(a))

    ans1 = len(triplets)

    part1_end_time = time.time()
    # Part 2


    longest = []
    for pc in connections:
        pos_longest = []
        for next in connections[pc]:
            if not pos_longest:
                pos_longest.append(next)
                continue
            fits = True
            for pos in pos_longest:
                if next not in connections[pos]:
                    fits = False
                    break
            if fits:
                pos_longest.append(next)
        pos_longest.append(pc)
        if len(pos_longest) > len(longest):
            longest = [a for a in pos_longest]
    
    l = sorted(longest)
    ans2 = ','.join([a for a in l])


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