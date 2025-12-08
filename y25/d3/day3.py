import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 3




def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    for batt_line in input.splitlines():
        batt_line_num = [int(a) for a in batt_line]
        largest = 0
        for i in range(len(batt_line_num)):
            if batt_line[i] < str(largest)[0]:
                continue
            for j in range(i+1,len(batt_line_num)):
                num = batt_line_num[i]*10 + batt_line_num[j]
                if num > largest:
                    largest = num
        ans1 += largest
    part1_end_time = time.time()
    # Part 2

    for batt_line in input.splitlines():
        batt_line_num = [int(a) for a in batt_line]
        if batt_line_num.count(9) >= 12:
            ans2 += 999999999999
            continue
        largest = 12*[0]
        indigits = 12*[0]
        for i in range(len(batt_line_num)-11):
            if batt_line_num[i] <= largest[0]:
                continue
            largest = 12*[0]
            indigits = 12*[0]
            indigits[0] = i
            largest[0] = batt_line_num[i]
            for digit in range(1, 12):
                for j in range(indigits[digit-1]+1,len(batt_line_num)-11+digit):
                    if batt_line_num[j] <= largest[digit]:
                        continue
                    largest[digit] = batt_line_num[j]
                    indigits[digit] = j
        l = ''
        for a in largest:
            l += str(a)
        ans2 += int(l)
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