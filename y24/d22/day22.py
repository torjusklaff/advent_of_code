import pathlib
from Tools.common import s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 22

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    all_bananas = []
    all_banana_diffs = []
    pos_sequences = set()
    for secret_start in input.splitlines():
        secret = int(secret_start)
        bananas_for_sale = [secret%10]
        for it in range(2000):
            temp = (secret*64^secret)%16777216
            temp2 = ((temp//32)^temp)%16777216
            secret = (temp2*2048^temp2)%16777216
            bananas_for_sale.append(secret%10)
        ans1 += secret
        all_bananas.append(bananas_for_sale)
        banana_diffs = {}
        for i in range(1,2001-4):
            b_diffs = ''
            for j in range(4):
                b_diffs += str(bananas_for_sale[i+j]-bananas_for_sale[i+j-1])
            if b_diffs not in banana_diffs:
                banana_diffs[b_diffs] = bananas_for_sale[i+3]
                
            pos_sequences.add(b_diffs)

        all_banana_diffs.append(banana_diffs)

    part1_end_time = time.time()

    # Part 2
    max_bananas = 0
    for pos_sequence in pos_sequences:
        pos_max = 0
        for b in range(len(all_banana_diffs)):
            try:
                pos_max += all_banana_diffs[b][pos_sequence]

            except Exception:
                if pos_max + (len(all_bananas) - b)*9 < max_bananas:
                    break
                continue
            
        if pos_max > max_bananas:
            max_bananas = pos_max


    ans2 = max_bananas





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