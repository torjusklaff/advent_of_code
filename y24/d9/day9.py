import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 9

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    part1 = False

    input = input.strip()
    l = []
    spaces = []
    nums = []
    index = 0
    dot_indices = []
    for i in range(len(input)):
        n = int(input[i])
        if i % 2 == 1:
            if n > 0:
                spaces.append([n,index])
        else:
            nums.append([n,index, i//2])
        for j in range(n):

            if i % 2 == 1:
                l.append('.')
                dot_indices.append(index+j)

            else:
                l.append(i//2)
        index += n

    dot_index = 0
    for i in range(len(l)-1, 1, -1):
        if dot_indices[dot_index] > i:
            break
        if l[i] != '.':
            l[dot_indices[dot_index]] = l[i]
            l[i] = '.'
            dot_index += 1

    for i in range(l.index('.')):
        ans1 += l[i]*i

    # Part 2
    for i in range(len(nums)-1, 0, -1):
        for j in range(len(spaces)):
            if spaces[j][1] > nums[i][1]:
                break
            if spaces[j][0] >= nums[i][0] and spaces[j][1] < nums[i][1]:
                nums[i][1] = spaces[j][1]
                spaces[j][1] += nums[i][0]
                spaces[j][0] -= nums[i][0]
                if spaces[j][0] == 0:
                    spaces.remove(spaces[j])
                break
        
    for p in nums:
        ans2 += sum([p[2]*(p[1]+b) for b in range(p[0])])


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