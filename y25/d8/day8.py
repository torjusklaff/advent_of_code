import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 8

def do(input, example):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1

    coords = []
    dists = {}
    sort = []
    num_coord = {}
    i = 0
    for line in input.splitlines():
        coords.append(tuple(s_to_int_list(line, ',')))
        num_coord[coords[-1]] = i
        i += 1
    
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            sorttime = (coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2 +  (coords[i][2] - coords[j][2])**2

            dists[sorttime] = num_coord[coords[i]], num_coord[coords[j]]
            sort.append(sorttime)
    sort = sorted(sort)
    if example:
        runs = 10
    else:
        runs = 1000
    circuits = []
    for i in range(runs):
        c1, c2 = dists[sort[i]]
        circuited = False
        for j in range(len(circuits)):
            if c1 in circuits[j] and c2 in circuits[j]:
                circuited = True
                break
            if c1 in circuits[j]:
                if circuited:
                    cir2 = circuits[j]
                    for c in cir:
                        if c not in cir2:
                            cir2 += [c]
                    circuits.pop(cj)
                    break
                cj = j
                cir = circuits[j]
                cir.append(c2)
                circuits[j] = cir
                circuited = True
            elif c2 in circuits[j]:
                if circuited:
                    cir2 = circuits[j]
                    for c in cir:
                        if c not in cir2:
                            cir2 += [c]

                    circuits[j] = list(cir2)
                    circuits.pop(cj)
                    break
                cir = circuits[j]
                cj = j
                cir.append(c1)
                circuits[j] = cir
                circuited = True
                
        if not circuited:
            circuits.append([c1, c2])

    completed_circuits = []
    for i in range(len(coords)):
        curr_cir = set([i])
        for circuit in circuits:
            if i in circuit:
                for c in circuit:
                    curr_cir.add(c)
        curr_cir = sorted(list(curr_cir))
        if curr_cir not in completed_circuits:
            completed_circuits.append(curr_cir)
    all_nodes = []
    for cir in completed_circuits:
        for c in cir:
            all_nodes.append(c)
    all_nodes = sorted(all_nodes)



    lens = sorted([len(a) for a in completed_circuits])
    len2 = sorted([len(a) for a in circuits])
    ans1 = lens[-1]*lens[-3]*lens[-2]
    ans1 = len2[-1]*len2[-3]*len2[-2]
    part1_end_time = time.time()
    # Part 2
    i = runs
    while True:
        c1, c2 = dists[sort[i]]
        circuited = False
        for j in range(len(circuits)):
            if c1 in circuits[j] and c2 in circuits[j]:
                circuited = True
                break
            if c1 in circuits[j]:
                if circuited:
                    cir2 = circuits[j]
                    for c in cir:
                        if c not in cir2:
                            cir2 += [c]
                    circuits.pop(cj)
                    break
                cj = j
                cir = circuits[j]
                cir.append(c2)
                circuits[j] = cir
                circuited = True
            elif c2 in circuits[j]:
                if circuited:
                    cir2 = circuits[j]
                    for c in cir:
                        if c not in cir2:
                            cir2 += [c]

                    circuits[j] = list(cir2)
                    circuits.pop(cj)
                    break
                cir = circuits[j]
                cj = j
                cir.append(c1)
                circuits[j] = cir
                circuited = True
        
        if not circuited:
            circuits.append([c1, c2])
        else:
            if len(cir) == len(coords) or len(cir2) == len(coords):
                ans2 = coords[c1][0]*coords[c2][0]
                break
        i += 1


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
    do(readfile(str(filepath)+"/input.txt"), False)

if __name__=="__main__":
    main()