import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 2

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0
    lmax = 1
    # Part 1
    for ran in input.split(','):
        start, end = ran.split('-')
        for num in range(int(start), int(end)+1):
            snum = str(num)
            l = len(snum)
            if l > lmax:
                lmax = l
            if l%2 == 0:
                if snum[:l//2] == snum[l//2::]:
                    ans1 += num
    part1_end_time = time.time()
    # Part 2
    # Så 2,4 mill tall
    for ran in input.split(','):
        start, end = ran.split('-')
        for num in range(int(start), int(end)+1):
            snum = str(num)
            l = len(snum)
            for i in range(1, l//2+1):
                if l%i == 0:
                    ccc = []
                    for j in range(l//i):
                        ccc.append(snum[i*j:i*j+i])
                    if len(set(ccc)) == 1:
                        ans2 += num
                        break
    part1_end_time = time.time()

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