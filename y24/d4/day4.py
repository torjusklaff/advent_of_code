import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 4

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0
    chart = []
    # Part 1
    for line in input:
        chart.append([a for a in line])
    for line in range(len(chart)):
        for letter in range(len(chart[line])):
            if chart[line][letter] == 'X':
                if letter + 3 < len(chart[line]):
                    if chart[line][letter+1]+chart[line][letter+2]+chart[line][letter+3] == 'MAS':
                        ans1 += 1
                if letter - 3 >= 0:
                    if chart[line][letter-1]+chart[line][letter-2]+chart[line][letter-3] == 'MAS':
                        ans1 += 1
                if line + 3 < len(chart):

                    if chart[line+1][letter]+chart[line+2][letter]+chart[line+3][letter] == 'MAS':
                        ans1 += 1
                if line - 3 >= 0:
                    if chart[line-1][letter]+chart[line-2][letter]+chart[line-3][letter] == 'MAS':
                        ans1 += 1
                if letter + 3 < len(chart[line]) and line + 3 < len(chart):

                    if chart[line+1][letter+1]+chart[line+2][letter+2]+chart[line+3][letter+3] == 'MAS':
                        ans1 += 1
                if letter + 3 < len(chart[line]) and line - 3 >= 0:
                    if chart[line-1][letter+1]+chart[line-2][letter+2]+chart[line-3][letter+3] == 'MAS':
                        ans1 += 1
                if letter - 3 >= 0 and line + 3 < len(chart):

                    if chart[line+1][letter-1]+chart[line+2][letter-2]+chart[line+3][letter-3] == 'MAS':
                        ans1 += 1
                if letter - 3 >= 0 and line - 3 >= 0:

                    if chart[line-1][letter-1]+chart[line-2][letter-2]+chart[line-3][letter-3] == 'MAS':
                        ans1 += 1

                
                



    # Part 2

    for line in range(1, len(chart) - 1):
        for letter in range(1, len(chart[line]) - 1):
            if chart[line][letter] == 'A':
                if chart[line-1][letter-1] == 'M' and chart[line-1][letter+1] == 'M' and chart[line+1][letter-1] == 'S' and chart[line+1][letter+1] == 'S':
                    ans2 += 1

                elif chart[line-1][letter-1] == 'S' and chart[line-1][letter+1] == 'M' and chart[line+1][letter-1] == 'S' and chart[line+1][letter+1] == 'M':
                    ans2 += 1

                elif chart[line-1][letter-1] == 'S' and chart[line-1][letter+1] == 'S' and chart[line+1][letter-1] == 'M' and chart[line+1][letter+1] == 'M':
                    ans2 += 1

                elif chart[line-1][letter-1] == 'M' and chart[line-1][letter+1] == 'S' and chart[line+1][letter-1] == 'M' and chart[line+1][letter+1] == 'S':
                    ans2 += 1


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