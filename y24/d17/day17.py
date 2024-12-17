import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 17

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    abc, inst = input.split('\n\n')
    q, inst = inst.split()

    A, B, C = s_to_pos_list(abc)
    A = int(A)
    B = int(B)
    C = int(C)
    instructions = s_to_int_list(inst, ',')

    combos = [0, 1, 2, 3, 4, 5, 6]

    s = ''

    i_pointer = 0
    while i_pointer < len(instructions):
        instruction = instructions[i_pointer]
        combo = combos[instructions[i_pointer+1]]
        if combo == 4:
            combo = A
        elif combo == 5:
            combo = B
        elif combo == 6:
            combo = C
        literal = instructions[i_pointer+1]
        if instruction == 0:
            A = int(A/2**combo)
        elif instruction == 1:
            B = B ^ literal
        elif instruction == 2:
            B = combo%8
        elif instruction == 3:
            if A != 0:
                i_pointer = literal
                continue
        elif instruction == 4:
            B = B ^ C
        elif instruction == 5:
            s += str(combo%8) + ','
        elif instruction == 6:
            B = int(A/2**combo)

        elif instruction == 7:
            C = int(A/2**combo)
        
        i_pointer += 2

    ans1 = s[:len(s)-1]
    
    s = ''


    part1_end_time = time.time()
    # Part 2
    current_total = 0

    for i in range(len(instructions)-1, -1, -1):
        digit = 8**i
        for j in range(8**(len(instructions)-i)):
            s = ''
            ans = []

            A = current_total + digit*j
            B = 0
            C = 0
            i_pointer = 0

            while i_pointer < len(instructions):
                instruction = instructions[i_pointer]
                literal = instructions[i_pointer+1]
                combo = combos[instructions[i_pointer+1]]
                if combo == 4:
                    combo = A
                elif combo == 5:
                    combo = B
                elif combo == 6:
                    combo = C
                if instruction == 0:
                    A = int(A/2**combo)
                elif instruction == 1:
                    B = B ^ literal
                elif instruction == 2:
                    B = combo%8
                elif instruction == 3:
                    if A != 0:
                        i_pointer = literal
                        continue
                elif instruction == 4:
                    B = B ^ C
                elif instruction == 5:
                    s += str(combo%8) + ','
                    ans.append(combo%8)
                    if len(ans) == i + 1 and ans[i] != instructions[i]:
                        break
                elif instruction == 6:
                    B = int(A/2**combo)

                elif instruction == 7:
                    C = int(A/2**combo)
                
                i_pointer += 2

            if len(ans) == len(instructions):
                if ans[i:] == instructions[i:]:
                    current_total += (8**i)*j
                    break
        
            
    ans2 = current_total

    # B = A % 8
    # B = B ^ 3
    # C = int(A/2**B)
    # B = B ^ C
    # B = B ^ 3
    # A = int(A/2**3)
    # print(B%8)
    # matchstring = '2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0'





    code_end_time = time.time()
    print("Part 1:\n{}".format(ans1))
    print("Part 2:\n{}".format(ans2))
    print("Time Part 1: \n{}".format(part1_end_time - code_start_time))
    print("Time Part 2: \n{}".format(code_end_time - part1_end_time))
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