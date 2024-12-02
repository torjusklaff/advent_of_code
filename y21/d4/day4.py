import pathlib
from Tools.common import readlinesfromfile, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 4

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    draws = s_to_int_list(input[0],',')
    boards = []
    ind = 0
    for i in range(2,len(input),6):
        ja = []
        for j in range(5):
            ja.append([[int(a), False] for a in input[i+j].split()])
        boards.append(ja)
    board_won = False
    for draw in draws:
        hit = False
        for board in boards:
            for line in range(len(board)):
                for pair in range(len(board[line])):
                    hit = False

                    if draw == board[line][pair][0]:
                        board[line][pair][1] = True
                        hit = True
                        break
                if hit: 
                    col, row = pair, line
                    break
            if hit:
                # bingo check 
                bingo = True
                for pair in board[row]:
                    if not pair[1]:
                        bingo = False
                        break
                if bingo:
                    win_board = board

                    board_won = True
                    break
                bingo = True

                for r in range(len(board)):
                    if not board[r][col][1]:
                        bingo = False
                        break
                if bingo:
                    win_board = board
                    board_won = True
                    break
        if board_won:
            win_draw = draw
            break        
    for line in win_board:
        for pair in line:
            if not pair[1]:
                ans1 += pair[0]
    ans1 *= win_draw

    # Part 2
    draws = s_to_int_list(input[0],',')
    boards = []
    ind = 0
    for i in range(2,len(input),6):
        ja = []
        for j in range(5):
            ja.append([[int(a), False] for a in input[i+j].split()])
        boards.append(ja)
    board_won = False
    draw = 0
    for draw in draws:
        won_boards = []
        board_won = False

        hit = False
        for board in boards:
            for line in range(len(board)):
                for pair in range(len(board[line])):
                    hit = False

                    if draw == board[line][pair][0]:
                        board[line][pair][1] = True
                        hit = True
                        break
                if hit: 
                    col, row = pair, line
                    break
            if hit:
                # bingo check 
                bingo = True
                for pair in board[row]:
                    if not pair[1]:
                        bingo = False
                        break
                if bingo:
                    board_won = True
                    if board not in won_boards:

                        won_boards.append(board)
                bingo = True

                for r in range(len(board)):
                    if not board[r][col][1]:
                        bingo = False
                        break
                if bingo:
                    board_won = True
                    if board not in won_boards:

                        won_boards.append(board)


        if board_won and len(boards) == 1:
            win_draw = draw
            break        

        for board in won_boards:
            boards.remove(board)

    for line in boards[0]:
        for pair in line:
            if not pair[1]:
                ans2 += pair[0]
    ans2 *= win_draw


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