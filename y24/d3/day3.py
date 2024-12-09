import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time
import re
 
day = 3

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0
    ah = re.compile('mul\(\d+,\d+\)')
    oh = re.compile("don\'t\(\).+mul\(\d+,\d+\).+do\(\)")
    oih = re.compile("don\'t\(\).+mul\(\d+,\d+\).+")

    # Part 1
    mul_pairs = []
    for line in input:
        it = ah.findall(line)
        for ar in it:
            a,b = ar.split(',')
            a = int(a.strip('mul('))
            b = int(b.strip(')'))
            mul_pairs.append((a,b))
    ans1 = sum([a*b for a,b in mul_pairs])
    # Part 2
    mul_pairs = []
    aaaaaah = ''
    for line in input:
        aaaaaah += line
    while True:
        try:
            x = None
            x = aaaaaah.index("don't()")
            y = aaaaaah[x:].index("do()")
            tap = aaaaaah[:x]
            ye = aaaaaah[x+y:]
            aaaaaah = tap + ye
        except ValueError:
            if x:
                aaaaaah = aaaaaah[:x]
            break    
    it = ah.findall(aaaaaah)
        # dont = oh.findall(line)
        # if dont:
        #     ds = [ah.findall(d) for d in dont]
        #     dont = [a for x in ds for a in x]
        # for d in dont:
        #     it.remove(d)
    for ar in it:
        a,b = ar.split(',')
        a = int(a.strip('mul('))
        b = int(b.strip(')'))
        mul_pairs.append((a,b))
    ans2 = sum([a*b for a,b in mul_pairs])

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