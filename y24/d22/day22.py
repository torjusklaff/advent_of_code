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
    all_banana_diffs = {}
    for secret_start in input.splitlines():
        secret = int(secret_start)
        bananas_for_sale = [secret%10]
        banana_diffs = {}
        diffs = []
        for it in range(2000):
            temp = (secret*64^secret)%16777216
            temp2 = ((temp//32)^temp)%16777216
            secret = (temp2*2048^temp2)%16777216
            bananas_for_sale.append(secret%10)
            diffs.append(str(bananas_for_sale[-1] - bananas_for_sale[-2]))
            if it > 2:
                diff_seq = ''.join(diffs[it-3:it+1])
                if diff_seq not in banana_diffs:
                    banana_diffs[diff_seq] = bananas_for_sale[-1]
        ans1 += secret
                
        for bdiff, tot in banana_diffs.items():
            try:
                all_banana_diffs[bdiff] += tot
            except KeyError:
                all_banana_diffs[bdiff] = tot

    part1_end_time = time.time()

    # Part 2

    max_bananas = 0
    for bdiff, tot in all_banana_diffs.items():
        if tot > max_bananas:
            max_bananas = tot

    print(len(all_banana_diffs))
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