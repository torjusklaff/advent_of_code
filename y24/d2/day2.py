import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 2

def pass_list(lis):
    found = True
    if lis[0] > lis[1]:
            for i in range(len(lis)-1):
                if lis[i] - lis[i+1] > 3 or lis[i] - lis[i+1] <= 0:
                    found = False
                    break

    elif lis[0] < lis[1]:
        for i in range(len(lis)-1):
            if lis[i+1] - lis[i] > 3 or lis[i+1] - lis[i] <= 0:
                found = False
                break
    else:
        found = False
        i = 0
    if found:
        return (True, i)
    return (False, i)
    
def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    for line in input:
        lis = s_to_int_list(line)
        found, i = pass_list(lis)

        if found:
            ans1 += 1
    


    # Part 2
    for line in input:
        lis = s_to_int_list(line)
        dampened = False
        found = True
        b = False

        found, i = pass_list(lis)
        if not found:
            lis1 = []
            lis2 = []
            for j in range(len(lis)):
                lis1 = [lis[a] for a in range(len(lis)) if a != j]
                found1, u = pass_list(lis1)
                if found1:
                    found = True
                    break
        if found:
            ans2 +=1
            
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