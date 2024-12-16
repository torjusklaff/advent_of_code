import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time
import re
day = 14

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    rmax = 103
    cmax = 101

    rmaxex = 103
    cmaxex = 101
    # Part 1
    q1,q2,q3,q4 = (0,0,0,0)
    lcms = []
    robots = []
    for robot in input.splitlines():
        nums = [int(x) for x in re.findall(r'-?\d+', robot)]
        robots.append(nums)
        pos = (nums[1], nums[0])
        r,c = pos
        r = (r + 100*nums[3])%rmaxex
        c = (c + 100*nums[2])%cmaxex
        
        if r < rmaxex//2 and c < cmaxex//2:
            q1 += 1
        elif r < rmaxex//2 and c > cmaxex//2:
            q2 += 1
        elif r > rmaxex//2 and c > cmaxex//2:
            q3 += 1
        elif r > rmaxex//2 and c < cmaxex//2:
            q4 += 1

        vis = set([(nums[1],nums[0])])
        pos = (nums[1],nums[0])
        i = 0
        # while True:
        #     r, c = pos
        #     r = (r + nums[3])%rmaxex
        #     c = (c + nums[2])%cmaxex
        #     i += 1
        #     if (r,c) in vis:
        #         break
        #     pos = (r,c)
        #     vis.add(pos)
    for i in range(rmax*cmax): 
        occ = set()
        found = True
        for robot in robots:
            
            r = (robot[1] + robot[3]*i)%rmaxex
            c = (robot[0] + robot[2]*i)%cmaxex
            pos = (r,c)
            if pos in occ:
                found = False
                break
            occ.add(pos)
        if found:
            for rr in range(rmax):
                s = ''
                for cc in range(cmax):
                    if (rr,cc) in occ:
                        s+='#'
                    else:
                        s+='.'
                print(s)
            print(i)
        
    ans1 = q1*q2*q3*q4




    # Part 2


    code_end_time = time.time()
    print("Part 1:\n{}".format(ans1))
    print("Part 2:\n{}".format(ans2))
    print("Time: \n{}\n".format(code_end_time - code_start_time))

    return

def main():
    print("\nDay: {}\n".format(day))
    print("Example: ")
    # do(readfile(str(filepath)+"/example.txt"))
    print("Input: ")
    do(readfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()