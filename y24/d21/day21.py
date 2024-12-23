import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 21

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1

    keypad = [[  '7','8','9'],
              [  '4','5','6'],
              [  '1','2','3'],
              [False,'0','A']]
    
    dirpad = [[False,'u','A'],
              [  'l','d','r']]
    
    keypad_dirs = {}
    dirpad_dirs = {
        ('u','A') : 'rA',
        ('u','d') : 'dA',
        ('u','r') : 'drA',
        ('u','l') : 'dlA',
        ('A','u') : 'lA',
        ('A','r') : 'dA',
        ('A','d') : 'ldA',
        ('A','l') : 'dllA',
        ('d','l') : 'lA',
        ('d','r') : 'rA',
        ('d','u') : 'uA',
        ('d','A') : 'urA',
        ('r','l') : 'llA',
        ('r','d') : 'lA',
        ('r','u') : 'luA',
        ('r','A') : 'uA',
        ('l','d') : 'rA',
        ('l','r') : 'rrA',
        ('l','u') : 'ruA',
        ('l','A') : 'rruA',
        ('A','A') : 'A',
        ('u','u') : 'A',
        ('l','l') : 'A',
        ('r','r') : 'A',
        ('d','d') : 'A',
    }
    
    for row in range(len(keypad)):
        for col in range(len(keypad[0])):
            curr = keypad[row][col]
            if not curr:
                continue
            for r in range(len(keypad)):
                for c in range(len(keypad[0])):
                    if r == row and c == col:
                        keypad_dirs[(curr,curr)] = 'A'
                        continue
                    next = keypad[r][c]
                    if not next: 
                        continue
                    direc = ''
                    steps = [r-row, c-col]
                    

                    if col == 0 and c > col and r == 3:
                        steps[1] -= 1
                        direc += 'r'
                    elif row == 3 and r < row and c < col:
                        direc += 'u'*abs(steps[0])
                        steps[0] = 0

                    if steps[1] < 0:
                        direc += 'l'*abs(steps[1])

                    if steps[0] > 0:
                        direc += 'd'*abs(steps[0])

                    if steps[0] < 0:
                        direc += 'u'*abs(steps[0])

                    if steps[1] > 0:
                        direc += 'r'*abs(steps[1])
                    direc += 'A'

                    keypad_dirs[(curr,next)] = direc
                    
    
    '''789
    456
    123
    x0A

    ^^^AvvA^<Avv>A
    <AAA>A
    v<<A>>^AAAvA^A


    ^A<<A^^>>AvvvA


    ^^<<A^>AvvvA>A

    ^^^<<A>A>AvvvA

    ^<<A'^^Av>>AvvA'''


    
    for code in input.splitlines():
        num = int(code[:3])
        dirs0 = keypad_dirs[('A', code[0])] + keypad_dirs[(code[0], code[1])] + keypad_dirs[(code[1], code[2])] + keypad_dirs[(code[2], code[3])]
        dirs1 = dirpad_dirs[('A', dirs0[0])]
        for i in range(len(dirs0) - 1):
            dirs1 += dirpad_dirs[(dirs0[i], dirs0[i+1])]
        dirs2 = dirpad_dirs[('A', dirs1[0])]
        for i in range(len(dirs1) - 1):
            dirs2 += dirpad_dirs[(dirs1[i], dirs1[i+1])]
        d = len(dirs2)
        ans1 += num * len(dirs2)
    '       u   A         ll      uu   A     rr   A        ddd      A'
    '   l   A r A  d ll   AA r  u AA r A  d  AA u A   l d  AAA r  u A'
    'ldlArruAdAuAldAlAArruAAdAluArAAdAuAldAruAAlArAldlArAruAAAdAluArA'
    '       u   A       uu        ll       A     rr   A        ddd      A'
    '   l   A r A   l   AA  d l   AA rr  u A  d  AA u A  d l   AAA u  r A'
    'dllArruAdAuAdllArruAAdlAlArruAAdAAluArAdlAurAAlArAdlAlArruAAAlAdrAuA'

    part1_end_time = time.time()
    # Part 2

    from functools import cache
    @cache
    def get_25th_dir(d1, d2, remaining):

        if remaining == 0:
            return len(dirpad_dirs[(d1,d2)])
        dd = 'A' + dirpad_dirs[(d1,d2)]

        dirs = 0

        for i in range(len(dd) - 1):
            dirs += get_25th_dir(dd[i],dd[i+1], remaining - 1)

        return dirs


    for code in input.splitlines():

        num = int(code[:3])
        keypad_to_dirpad_dirs = 'A' + keypad_dirs[('A', code[0])] \
            + keypad_dirs[(code[0], code[1])] \
            + keypad_dirs[(code[1], code[2])] \
            + keypad_dirs[(code[2], code[3])]
        
        num_dirs = 0
        for i in range(len(keypad_to_dirpad_dirs)-1):
            num_dirs = get_25th_dir(keypad_to_dirpad_dirs[i], keypad_to_dirpad_dirs[i+1], 24)

        ans2 += num * num_dirs
        
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
    do(readfile(str(filepath)+"/example.txt"))
    print("Input: ")
    do(readfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()