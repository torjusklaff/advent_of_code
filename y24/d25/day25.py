import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 25

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    keys = []
    locks = []
    for gr in input.split('\n\n'):
        gr = gr.splitlines()
        gr = [[c for c in r] for r in gr]
        heights = []
        if gr[0][0] == '#':
            for c in range(5):
                height = 0
                for r in range(6):
                    if gr[r][c] == '.':
                        break
                    height += 1
                heights.append(height)
            locks.append(heights)
        else:
            for c in range(5):
                height = 0
                for r in range(6, -1, -1):
                    if gr[r][c] == '.':
                        break
                    height += 1

                heights.append(height)
            keys.append(heights)
    for lock in locks:
        for key in keys:
            match = True
            for i in range(5):
                if key[i] + lock[i] > 7:
                    match = False
                    break
            if match:
                ans1 += 1


    part1_end_time = time.time()
    # Part 2


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