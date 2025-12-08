import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 7

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    start = input.splitlines()[0].index('S')
    q = [start]
    for line in input.splitlines():
        nextq = set()
        while q:
            index = q.pop(0)
            if line[index] == '.':
                nextq.add(index)
            else:
                nextq.add(index - 1)
                nextq.add(index + 1)
                ans1 += 1
        q = list(nextq)

    part1_end_time = time.time()
    # Part 2
    lines = input.splitlines()
    q = [0]*len(lines[0])
    q[start] = 1
    for line in input.splitlines()[1::]:

        nextq = [a for a in q]
        for j in range(len(q)):
            if q[j] > 0:
                if line[j] == '^':
                    nextq[j-1] += q[j]
                    nextq[j+1] += q[j]
                    nextq[j] = 0
        q = list(nextq)
    ans2 = sum(q)

    # q = [(0, start)]

    # while q:
    #     lin, ind = q.pop(0)
    #     for i in range(lin + 1, len(lines)):
    #         if lines[i][ind] == '^':
    #             ind -= 1
    #             q.append((i,ind + 2))
    #     ans2 += 1



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