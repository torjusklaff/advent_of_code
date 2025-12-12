import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 10

def do(input, example):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    max_len = 0
    for line in input.splitlines():
        bulk = line.split(' ')
        goal = bulk.pop(0)[1:-1]
        goal = [1 if g == '#' else 0 for g in goal]
        joltages = s_to_int_list(bulk.pop(-1)[1:-1],',')
        buttons = []
        for button in bulk:
            buttons.append(eval(button))
        found = False
        its = 0
        from itertools import combinations_with_replacement
        while not found:
            its += 1
            combs = combinations_with_replacement(buttons, its)
            for comb in combs:
                state = [0]*len(goal)
                for button in comb:
                    if isinstance(button, int):
                        state[button] = (state[button]+1)%2
                    else:
                        for b in button:
                            state[b] = (state[b]+1)%2
                if state == goal:
                    found = True
                    ans1 += its
                    break
        if len(goal) > max_len:
            max_len = len(goal)
            max_butts = len(buttons)
                
    part1_end_time = time.time()
    # Part 2
    min_tot_pushes = 0
    max_tot_pushes = 0
    from scipy.optimize import linprog
    for line in input.splitlines():
        bulk = line.split(' ')
        goal = bulk.pop(0)[1:-1]
        goal = [1 if g == '#' else 0 for g in goal]
        joltages = s_to_int_list(bulk.pop(-1)[1:-1],',')
        buttons = []
        for button in bulk:
            buttons.append(eval(button))

        better_buttons = []
        for button in buttons:
            nb = [0]*len(joltages)
            if isinstance(button, int):
                nb[button] = 1
                better_buttons.append(nb)
                continue
            for i in button:
                    nb[i] = 1
            better_buttons.append(nb)
            
        min_pushes = sum(joltages)
        max_tot_pushes += min_pushes
        min_tot_pushes += max(joltages)

        transposed_buttons = [[better_buttons[i][j] for i in range(len(better_buttons))] for j in range(len(better_buttons[0])) ]

        obj = [1]*len(better_buttons)
        lhs_eq = transposed_buttons
        rhs_eq = joltages
        bnd =[(0,max(joltages))]*len(better_buttons)
        integ = [1]*len(better_buttons)
        opt = linprog(c=obj,A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd, integrality=integ)
        ans2 += int(opt.fun)

        
        
    

        
        


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
    do(readfile(str(filepath)+"/example.txt"), True)
    print("Input: ")
    do(readfile(str(filepath)+"/input.txt"), False)

if __name__=="__main__":
    main()