import pathlib
from Tools.common import readfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 6

def do(input):
    code_start_time = time.time()

    dirs = {'u': (-1,0), 'r':(0,1), 'd':(1,0), 'l':(0,-1), }
    dir_list = ['u','r','d','l']
    diri = 0

    ans1 = 0
    ans2 = 0

    input = input.splitlines()

    # Part 1
    maze = []
    for line in range(len(input)):
        maze.append([])
        for dot in range((len(input[0]))):
            if input[line][dot] == '^':
                start = (line, dot)
                maze[line].append('.')
            else:
                maze[line].append(input[line][dot])
    visited = set([start])
    d = 'u'
    pos = start
    while True:
        x, y = pos
        d = dir_list[diri%len(dir_list)]
        xn, yn = dirs[d]
        if x + xn >= len(maze) or x + xn < 0 or y + yn >= len(maze[0]) or y + yn < 0:
            break

        if maze[x+xn][y+yn] == '#':
            diri += 1
        else:
            pos = (x+xn, y+yn)

        visited.add(pos)
    ans1 = len(visited)
    

    # Part 2
    
    for a in visited:
        if a != start:
            v = set()
            diri = 0 
            pos = start
            while True:
                x, y = pos
                d = dir_list[diri%len(dir_list)]
                xn, yn = dirs[d]

                if x + xn >= len(maze) or x + xn < 0 or y + yn >= len(maze[0]) or y + yn < 0:
                    break
                if (x+xn,y+yn,d) in v:
                    ans2 += 1
                    break

                if maze[x+xn][y+yn] == '#' or (x+xn,y+yn) == a:
                    diri += 1
                    d = dir_list[diri%len(dir_list)]

                else:
                    pos = (x+xn, y+yn)
                    
                v.add((x,y,d))


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