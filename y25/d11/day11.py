import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 11

def do(input, example):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    connections = {}
    for line in input.splitlines():
        key, res = line.split(': ')
        connections[key] = res.split(' ')
    q = [c for c in connections['you']]
    while q:
        point = q.pop(0)
        for n in connections[point]:
            if n == 'out':
                ans1 += 1
            else:
                q.append(n)
    part1_end_time = time.time()
    # Part 2

    # split it up? Works on some!
    svrdac = 0
    svrfft = 0
    dacfft = 0
    dacout = 0
    fftdac = 0
    fftout = 0
    
    # if example:
    #     return

    followers = {}
    followers['out'] = set()
    for server in connections.keys():
        q = [c for c in connections[server]]
        follower = set(connections[server])
        if 'out' in follower:
            q = []
            follower = set()
        while q:
            conn = q.pop(0)

            for c in connections[conn]:
                if c in followers:
                    follower.update(followers[c])
                    continue
                if c not in follower:
                    follower.add(c)
                    if c != 'out':
                        q.append(c)
        followers[server] = follower

    
    q = [[c] for c in connections['dac']]
    avoid_from_dac = set()
    while q:
        points = q.pop(0)
        point = points[-1]
        avoid_from_dac.add(point)
        if point == 'out':
            continue
        for n in connections[point]:
            if n == 'fft':
                dacfft += 1
            elif n == 'out':
                dacout += 1
            elif n in points:
                continue
            else:
                q.append(points + [n])

    q = [c for c in connections['fft']]
    for follower in followers['fft']:
        if follower in avoid_from_dac or follower == 'dac':
            continue
        if 'dac' not in followers[follower]:
            avoid_from_dac.add(follower)

    q = [c for c in connections['fft']]
    # while q:
    #     point = q.pop(-1)
    #     if point == 'out':
    #         continue
    #     if point in avoid_from_dac:
    #         continue
    #     for n in connections[point]:
    #         if n == 'dac':
    #             dacout += 1
    #         else:
    #             q.append(n)
    # for follower in followers['svr']:
    #     if follower in avoid_from_dac or follower == 'fft':
    #         continue
    #     if 'fft' not in followers[follower]:
    #         avoid_from_dac.add(follower)


    from functools import cache

    @cache
    def dfs(taken_steps, fft, dac, current):
        if current == 'out':
            if fft and dac:
                return 1
            else:
                return 0
        total = 0
        if current == 'fft':
            fft = True
        elif current == 'dac':
            dac = True
        
        for n in connections[current]:

            total += dfs(taken_steps + 1, fft, dac, n)
        return total
    ans2 = dfs(0, False, False, 'svr')
    

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