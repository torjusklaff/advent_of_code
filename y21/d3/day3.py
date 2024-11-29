import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list, bin_string_to_int
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 3

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    eps = ''
    gamm = ''

    for i in range(len(input[0])):
        s = ''
        for line in input:
            s += line[i]
        if s.count('1') > s.count('0'):
            gamm += '1'
            eps += '0'
        else:
            gamm += '0'
            eps += '1'


    ans1 = bin_string_to_int(eps)*bin_string_to_int(gamm)
    # Part 2
    ox = [i for i in input]
    co2 = [i for i in input]
    for i in range(len(input[0])):
        so = ''
        sco = ''
        for line in ox:
            so += line[i]
        for line in co2:
            sco += line[i]
        if len(sco) > 1:
            if sco.count('1') >= sco.count('0'):
                co2 = [co for co in co2 if co[i] == '0']
            else:            
                co2 = [co for co in co2 if co[i] == '1']
        if len(so) > 1:
            if so.count('1') >= so.count('0'):
                ox = [co for co in ox if co[i] == '1']
            else:            
                ox = [co for co in ox if co[i] == '0']
    ans2 = bin_string_to_int(ox[0])*bin_string_to_int(co2[0])



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