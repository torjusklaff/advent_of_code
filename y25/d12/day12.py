import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 12

def do(input, example):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    parts = input.split('\n\n')
    tree_grids = parts.pop(-1)
    presents = []
    areas = []
    max_areas = []
    for part in parts:
        lines = part.splitlines()
        present = [line for line in lines[1:]]
        presents.append(present)
        area = 0
        for line in present:
            area += line.count('#')
        areas.append(area)
        max_areas.append(len(present)*len(present[0]))
    

    
    for tree_grid in tree_grids.splitlines():
        size, nums = tree_grid.split(': ')
        cols, rows = s_to_int_list(size,'x')
        nums = s_to_int_list(nums)
        needed_area = sum([a*n for a,n in zip(areas,nums)])
        if needed_area > cols*rows:
            continue
        max_area_of_presents = sum([a*n for a,n in zip(max_areas,nums)])
        if max_area_of_presents <= cols*rows:
            ans1 += 1
            continue
        
        # Here I would do the packing if I had time    
        ans2 += 1
    part1_end_time = time.time()
    # Part 2


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