import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 7

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    n = 0
    # Part 1
    for line in input.splitlines():
        a,b = line.split(': ')
        nums = s_to_int_list(b)

        conc_pos = False
        mult_pos = False
        Found = False

        if a.endswith(str(nums[-1])):
            conc_pos = True

        a = int(a)

        if a%nums[-1] == 0:
            mult_pos = True

        for i in range(2**(len(nums)-1)):
            tot = nums[0]
            for j in range(1, len(nums)):
                if (i//2**(j-1))%2 == 0:
                    tot += nums[j]
                else:
                    tot *= nums[j]
                if tot > a:
                    break
            if tot == a:
                ans1 += a
                ans2 += a
                Found = True
                break

        if Found:
            continue

        for i in range(3**(len(nums)-2)):
            part1 = True
            tot = nums[0]
            for j in range(1, len(nums)-1):
                if (i//3**(j-1))%3 == 0:
                    tot += nums[j]
                elif (i//3**(j-1))%3 == 1:
                    tot *= nums[j]
                else:
                    tot = int(str(tot)+str(nums[j]))
                if tot > a:
                    break
            tots = [tot + nums[-1]]
            if mult_pos:
                tots.append(tot*nums[-1])
            if conc_pos:
                tots.append(int(str(tot)+str(nums[-1])))
            for to in tots:
                if to == a:
                    ans2 += a
                    Found = True
                    break

            if Found:
                break
            


    # Part 2
    print(n)

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