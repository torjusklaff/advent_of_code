from collections import defaultdict
import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 13

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    input = input.splitlines()
    for i in range(0,len(input), 4):
        a = input[i]
        b = input[i+1]
        prize = input[i+2]
        ax, ay = a.split(',')
        ax = int(ax.split('+')[1])
        ay = int(ay.split('+')[1])
        bx, by = b.split(',')
        bx = int(bx.split('+')[1])
        by = int(by.split('+')[1])
        px, py = prize.split(',')
        px = int(px.split('=')[1])
        py = int(py.split('=')[1])

        # lowest = 401
        # l = 401
        # for a in range(100):
        #     if (ax*a > px) or (ay*a > py):
        #         break
        #     for b in range(100):
        #         if (ax*a + bx*b > px) or (ay*a + by*b > py):
        #             break
        #         if (ax*a + bx*b == px) and (ay*a + by*b == py):
        #             l = 3*a + b
        #             break
        #     if l < lowest:
        #         lowest = l
        #         break
        # if lowest < 401:
        #     ans1 += lowest

        b = (px*ay - ax*py)/(bx*ay - ax*by)
        a = (py -by*b)/ay

        if a == int(a) and b == int(b) and b <= 100 and a <= 100:        
            ans1 += b + 3*a

    # Part 2

        px += 10000000000000
        py += 10000000000000

        b = (px*ay - ax*py)/(bx*ay - ax*by)
        a = (py -by*b)/ay
        if a > int(a) or b > int(b):
            continue

        ans2 += b + 3*a



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