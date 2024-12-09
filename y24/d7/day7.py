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
    for line in input.splitlines():
        a,b = line.split(': ')
        nums = s_to_int_list(b)

        a = int(a)
        for i in range(3**(len(nums)-1)):
            part1 = True
            tot = nums[0]
            for j in range(1, len(nums)):
                if (i//3**(j-1))%3 == 0:
                    tot += nums[j]
                elif (i//3**(j-1))%3 == 1:
                    tot *= nums[j]
                else:
                    tot = int(str(tot)+str(nums[j]))
                    part1 = False
            if tot == a:
                if part1:
                    ans1 += a
                ans2 += a
                break


    # Part 2


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