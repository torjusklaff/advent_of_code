import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile, bin_string_to_int
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 24

def do(input, example = False):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    values = {}
    val2es = {}
    xes = []
    ys = []
    initial_values, gates = input.split('\n\n')
    for iv in initial_values.splitlines():
        var, val = iv.split(': ')
        values[var] = 1
        val2es[var] = 1

        if var[0] == 'x':
            # val2es[var] = 0
            # values[var] = 0
            xes.append(var)
        elif var[0] == 'y':
            ys.append(var)
    xes = sorted(xes)
    ys = sorted(ys)

    bin_x = ''
    bin_y = ''
    for x in xes[-1::-1]:
        bin_x += str(values[x])
    for y in ys[-1::-1]:
        bin_y += str(values[y])

    e_z_dict = {}


    logic_gates = {}
    l_gates_2 = {}
    q = []
    start_q = []
    gate_list = []
    for gate in gates.splitlines():
        v1, op, v2, ss, end = gate.split()
        logic_gates[end] = (v1, op, v2)
        l_gates_2[end] = (v1, op, v2)
        gate_list.append(end)
        if v1 in values and v2 in values:
            q.append(end)
            start_q.append(end)
        if end[0] == 'z':
            e_z_dict[end] = '0'


    
    expected_z = bin_string_to_int(bin_x) + bin_string_to_int(bin_y)
    e_z = format(expected_z, 'b')
    if len(e_z) < len(e_z_dict):
        e_z = '0'*(len(e_z_dict)-len(e_z)) + e_z
    for i in range(len(e_z) - 1, -1, -1):
        e_z_dict['z' + str(i)] = e_z[len(e_z)-i - 1]
    
    while logic_gates:
        while q:
            e = q.pop(0)
            v1, op, v2 = logic_gates[e]
            if op == 'AND':
                values[e] = values[v1] & values[v2]
            elif op == 'OR':
                values[e] = values[v1] | values[v2]
            else:
                values[e] = values[v1] ^ values[v2]
            logic_gates.pop(e, None)
        for (e, (v1, op, v2)) in logic_gates.items():
            if v1 in values and v2 in values:
                q.append(e)

    zeds = []
    for v in values:
        if v[0] == 'z':
            zeds.append(v)
    zeds = sorted(zeds)
    binary_val = ''
    for z in zeds[-1::-1]:
        binary_val += str(values[z])
    
    ans1 = bin_string_to_int(binary_val)


    part1_end_time = time.time()
    # Part 2

    def get_op_list(z):
        (v1, op, v2) = l_gates_2[z]
        if v1 in val2es and v2 in val2es:
            return v1 + ' ' + op + ' ' + v2
        return get_op_list(v1) + ' ' + op + ' ' + get_op_list(v2)
    
    bits = len(e_z)
    op_lists = {}
    for l_gate in l_gates_2:
        if l_gate[0] != 'z':
            continue
        # if l_gate == 'z16':
        #     print(l_gates_2[l_gate])
        # z_ind = int(l_gate[1:])
        # if binary_val[bits-z_ind] == e_z[bits-z_ind]:
        #     continue
        # (v1, op, v2) = l_gates_2[l_gate]
        l = get_op_list(l_gate)
        print(l_gate, len(l.split()))
        op_lists[l_gate] = l

    i = 0

    logic_gates = l_gates_2
    values = val2es
    poor_combos = []
    poor_op_lists = {}
    for (end, (v1, op, v2)) in logic_gates.items():
        if end[0] == 'z':
            if op != 'XOR' and int(end[1:]) < len(e_z) - 1:
                poor_combos.append(end)
        elif (v1 not in values or v2 not in values) and op == 'XOR':
            poor_combos.append(end)
    for pc in poor_combos:
        l = get_op_list(pc)
        poor_op_lists[pc] = l

    swaps = [('z39', 'mqh'), ('z08', 'vvr'), ('z28', 'tfb'), ('rnq', 'bkr')]
    #, , ('z16','kbg')
    for s, w in swaps:
        l = l_gates_2[w]
        d = l_gates_2[s]
        logic_gates[s] = l
        logic_gates[w] = d
    
    wrong_z_last = 'z16'

    for l_gate in logic_gates:
        if 'x16' in logic_gates[l_gate] or 'y16' in logic_gates[l_gate]:
            print(l_gate)
            print(logic_gates[l_gate])
            
            l3 = get_op_list(l_gate)

    while logic_gates:
        while q:
            e = q.pop(0)
            v1, op, v2 = logic_gates[e]
            if op == 'AND':
                values[e] = values[v1] & values[v2]
            elif op == 'OR':
                values[e] = values[v1] | values[v2]
            else:
                values[e] = values[v1] ^ values[v2]
            
            logic_gates.pop(e, None)
        for (e, (v1, op, v2)) in logic_gates.items():
            if v1 in values and v2 in values:
                q.append(e)

    zeds = []
    for v in values:
        if v[0] == 'z':
            zeds.append(v)
    zeds = sorted(zeds)
    binary_val = ''
    for z in zeds[-1::-1]:
        binary_val += str(values[z])

    l = []
    for a, b in swaps:
        l.append(a)
        l.append(b)
    l = sorted(l)
    ans2 = ','.join([la for la in l])
    print(e_z)
    print(binary_val)
    # import itertools
    # g_list = [g for g in gate_list if g not in poor_combos]

    # pairs = list(itertools.product(g_list, g_list))
    # pairs = [p for p in pairs if p[0] != p[1]]
    # pps = set()
    # for p in pairs:
    #     if (p[1], p[0]) not in pps:
    #         pps.add(p)

    # pairs = list(pps)
    # pairs = [p for p in pairs if p[0] not in logic_gates[p[1]] and p[1] not in logic_gates[p[0]] ]
    # if example:
    #     return
    # while binary_val != e_z:
    #     found = True
    #     g_list = [g for g in gate_list]
    #     q = [s for s in start_q]
    #     swaps = {}
    #     swap_pairs = next(combs)

    #     for a, b in swap_pairs:
    #         swaps[a] = b
    #         swaps[b] = a
    #     if len(swaps) < 8:
    #         continue


    #     while g_list:
    #         while q:
    #             e = q.pop(0)
    #             v1, op, v2 = logic_gates[e]
    #             g_list.remove(e)

    #             if e in swaps:
    #                 e = swaps[e]

    #             if op == 'AND':
    #                 values[e] = values[v1] & values[v2]
    #             elif op == 'OR':
    #                 values[e] = values[v1] | values[v2]
    #             else:
    #                 values[e] = values[v1] ^ values[v2]
    #             if e in e_z_dict and values[e] != e_z_dict[e]:
    #                 found = False
    #                 break
    #         if not found:
    #             break
    #         for g in g_list:
    #             v1, op, v2 = logic_gates[g]
    #             if v1 in values and v2 in values:
    #                 q.append(g)
    #     binary_val = ''
    #     for z in zeds[-1::-1]:
    #         u = values.pop(z, '0')
    #         binary_val += str(u)
    #     i += 1

        
        




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
    # do(readfile(str(filepath)+"/example.txt"), True)
    print("Input: ")
    do(readfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()