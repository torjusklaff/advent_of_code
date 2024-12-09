import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 5

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    musts = {}
    for line in input:
        if line == '':
            ind = input.index(line)+1
            break
        oh = s_to_int_list(line,'|')
        if oh[0] not in musts.keys():
            musts[oh[0]] = [oh[1]]
        else:
            musts[oh[0]].append(oh[1])
    lists = []
    for line in input[ind:]:
        lists.append(s_to_int_list(line,','))
    incorrect = []
    wrong_id = []
    for l in lists:
        correct = True
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                if l[i] in musts.keys() and l[j] not in musts[l[i]]:
                    incorrect.append(l)
                    correct = False
                    break
                if l[j] in musts.keys() and l[i] in musts[l[j]]:
                    incorrect.append(l)
                    correct = False
                    break
            if not correct:
                break
        if correct:
            ans1 += l[len(l)//2]


    # Part 2

    for l in incorrect:
        temp = [0]*len(l)
        for i in l:
            ind = 0
            for j in [a for a in l if a != i]:
                if j in musts.keys() and i in musts[j]:
                    ind += 1
            temp[ind] = i
        ans2 += temp[len(l)//2]
        


    code_end_time = time.time()
    print("Part 1: ")
    print(ans1)
    print("Part 2: ")
    print(ans2)
    print("Time: ", code_end_time - code_start_time)
    return

def main():
    print()
    print("Day: ", day)
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print()
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))
    print()

if __name__=="__main__":
    main()